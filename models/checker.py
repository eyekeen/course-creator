from .tests import Test
from .answers import Answer
from .answersresultsdeltas import AnswersResultsDeltas
from .db_session import create_session
from .testsrightanswers import TestsRightAnswers
from .testsloseanswers import TestLoseAnswers
from .questionsrightanswers import QuestionsRightAnswers


class OptionalCheckerFactory:

    def __init__(self, test):
        self.test = test

    def check(self, user_answers: list[Answer]):
        scores = {i: 0 for i in self.test.results}
        sess = create_session()
        for ind, question in enumerate(self.test.questions):
            for result in self.test.results:
                delta = sess.query(AnswersResultsDeltas).filter(
                    AnswersResultsDeltas.answer_id == user_answers[ind]).filter(
                    AnswersResultsDeltas.result_id == result.id).first().delta
                scores[result] += delta
        return max(scores.items(), key=lambda x: x[1])[0]


class AssesmentCheckerFactory:
    def __init__(self, test):
        self.test = test
    def check(self, user_answers):
        lose_ans_num = 0
        right_ans_num = 0
        sess = create_session()
        for ind, q in enumerate(self.test.questions):
            right_answer = sess.query(QuestionsRightAnswers).filter(QuestionsRightAnswers.question_id == q.id).first()
            if right_answer.rightanswer_id == user_answers[ind].id:
                right_ans_num += 1
            else:
                lose_ans_num += 1
        points_for_rights = sess.query(TestsRightAnswers).filter(TestsRightAnswers.test_id == self.test.id).filter(
            TestsRightAnswers.rightanswersnum == right_ans_num).first().fine
        points_for_loses = sess.query(TestLoseAnswers).filter(TestLoseAnswers.test_id == self.test.id).filter(
            TestLoseAnswers.loseanswersnum == lose_ans_num).first().fine
        return points_for_rights - points_for_loses


class CheckerFactory:
    @staticmethod
    def create(test) -> AssesmentCheckerFactory | OptionalCheckerFactory:
        if test.type_id == 0:
            return OptionalCheckerFactory(test)
        return AssesmentCheckerFactory(test)

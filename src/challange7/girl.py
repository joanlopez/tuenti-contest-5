#!/usr/bin/env python


class Girl:
    def __init__(self, name, answers):
        self.name = name
        self.answers = answers
        self.points = 0
        self.friends = []

    def count_points(self):
        self._treat_question_a(self.answers['A'])
        self._treat_question_b()
        self._treat_question_c()
        self._treat_question_d()
        return self.points

    def _treat_question_a(self, answer):
        if answer == 'Y':
            self.points += 7

    def _treat_question_b(self):
        for friend in self.friends:
            if friend.like_super_heroes():
                self.points += 3

    def _treat_question_c(self):
        for friend in self.friends:
            for friend_of in friend.friends:
                if friend_of is not self \
                        and friend_of not in self.friends \
                        and friend_of.like_leisure_suits():
                    self.points += 6

    def _treat_question_d(self):
        for friend in self.friends:
            if friend.like_cats():
                check = True
                for friend_of in friend.friends:
                    if friend_of is not self \
                            and friend_of.like_cats():
                        check = False
                        break
                if check:
                    self.points += 4
                    break

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def like_super_heroes(self):
        return self.answers['B'] == 'Y'

    def like_leisure_suits(self):
        return self.answers['C'] == 'Y'

    def like_cats(self):
        return self.answers['D'] == 'Y'

    def like_shopping(self):
        return self.answers['E'] == 'Y'
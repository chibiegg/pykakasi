# -*- coding: utf-8 -*-
import unittest
import pykakasi

class TestPyKakasi(unittest.TestCase):

    def test_J2H(self):

        TESTS = [
            (u"構成",         (u"こうせい",2)),
            (u"好き",          (u"すき",2)),
            (u"大きい",       (u"おおき",2)),
      ]

        I_TEST = [
            (u"菟", u"兎"),
            (u"菟集", u"兎集"),
            (u"熙", u"煕"),
        ]

        j = pykakasi.J2H()
        for case, result in TESTS:
            self.failUnlessEqual(j.convert(case), result)
        for case, result in I_TEST:
            self.failUnlessEqual(j.itaiji_conv(case), result)

    def test_H2a(self):

        TESTS = [
            (u"かんたん",   ("ka", 1)),
            (u"にゃ", ("nya",2)),
            (u"っき", ("kki",2)),
            (u"っふぁ", ("ffa", 3)),
        ]

        h = pykakasi.H2a()
        for case, result in TESTS:
            self.failUnlessEqual(h.convert(case), result)

    def test_kakasi(self):

        TESTS = [
            (u"構成",         "kousei"),
            (u"好き",          "suki"),
            (u"大きい",       "ookii"),
            (u"かんたん",  "kantan"),
            (u"にゃ",          "nya"),
            (u"っき",           "kki"),
            (u"っふぁ",        "ffa"),
        ]

        k = pykakasi.kakasi()
        for case, result in TESTS:
            self.failUnlessEqual(k.do(case), result)


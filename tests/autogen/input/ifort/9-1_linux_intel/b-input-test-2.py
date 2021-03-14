
import sys
import os
import unittest
from nose.plugins.attrib import attr

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class BEditDescriptorBatch2TestCase(unittest.TestCase):

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_1(self):
        inp = '''-100000'''
        fmt = '''(1B1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_2(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_3(self):
        inp = '''10101000'''
        fmt = '''(1B1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_4(self):
        inp = '''0'''
        fmt = '''(1B2.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_5(self):
        inp = '''-0'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_6(self):
        inp = '''1'''
        fmt = '''(1B2.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_7(self):
        inp = '''-1'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_8(self):
        inp = '''2'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_9(self):
        inp = '''10'''
        fmt = '''(1B2.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_10(self):
        inp = '''-10'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_11(self):
        inp = '''100'''
        fmt = '''(1B2.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_12(self):
        inp = '''-100'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_13(self):
        inp = '''1000'''
        fmt = '''(1B2.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_14(self):
        inp = '''-1000'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_15(self):
        inp = '''10000'''
        fmt = '''(1B2.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_16(self):
        inp = '''-10000'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_17(self):
        inp = '''100000'''
        fmt = '''(1B2.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_18(self):
        inp = '''-100000'''
        fmt = '''(1B2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_19(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B2.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_20(self):
        inp = '''10101000'''
        fmt = '''(1B2.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_21(self):
        inp = '''0'''
        fmt = '''(1B3.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_22(self):
        inp = '''-0'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_23(self):
        inp = '''1'''
        fmt = '''(1B3.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_24(self):
        inp = '''-1'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_25(self):
        inp = '''2'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_26(self):
        inp = '''10'''
        fmt = '''(1B3.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_27(self):
        inp = '''-10'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_28(self):
        inp = '''100'''
        fmt = '''(1B3.0)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_29(self):
        inp = '''-100'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_30(self):
        inp = '''1000'''
        fmt = '''(1B3.0)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_31(self):
        inp = '''-1000'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_32(self):
        inp = '''10000'''
        fmt = '''(1B3.0)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_33(self):
        inp = '''-10000'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_34(self):
        inp = '''100000'''
        fmt = '''(1B3.0)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_35(self):
        inp = '''-100000'''
        fmt = '''(1B3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_36(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B3.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_37(self):
        inp = '''10101000'''
        fmt = '''(1B3.0)'''
        result = [5]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_38(self):
        inp = '''0'''
        fmt = '''(1B5.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_39(self):
        inp = '''-0'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_40(self):
        inp = '''1'''
        fmt = '''(1B5.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_41(self):
        inp = '''-1'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_42(self):
        inp = '''2'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_43(self):
        inp = '''10'''
        fmt = '''(1B5.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_44(self):
        inp = '''-10'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_45(self):
        inp = '''100'''
        fmt = '''(1B5.0)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_46(self):
        inp = '''-100'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_47(self):
        inp = '''1000'''
        fmt = '''(1B5.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_48(self):
        inp = '''-1000'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_49(self):
        inp = '''10000'''
        fmt = '''(1B5.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_50(self):
        inp = '''-10000'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_51(self):
        inp = '''100000'''
        fmt = '''(1B5.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_52(self):
        inp = '''-100000'''
        fmt = '''(1B5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_53(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B5.0)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_54(self):
        inp = '''10101000'''
        fmt = '''(1B5.0)'''
        result = [21]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_55(self):
        inp = '''0'''
        fmt = '''(1B10.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_56(self):
        inp = '''-0'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_57(self):
        inp = '''1'''
        fmt = '''(1B10.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_58(self):
        inp = '''-1'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_59(self):
        inp = '''2'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_60(self):
        inp = '''10'''
        fmt = '''(1B10.0)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_61(self):
        inp = '''-10'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_62(self):
        inp = '''100'''
        fmt = '''(1B10.0)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_63(self):
        inp = '''-100'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_64(self):
        inp = '''1000'''
        fmt = '''(1B10.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_65(self):
        inp = '''-1000'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_66(self):
        inp = '''10000'''
        fmt = '''(1B10.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_67(self):
        inp = '''-10000'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_68(self):
        inp = '''100000'''
        fmt = '''(1B10.0)'''
        result = [32]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_69(self):
        inp = '''-100000'''
        fmt = '''(1B10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_70(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B10.0)'''
        result = [66]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_71(self):
        inp = '''10101000'''
        fmt = '''(1B10.0)'''
        result = [168]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_72(self):
        inp = '''0'''
        fmt = '''(1B3.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_73(self):
        inp = '''-0'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_74(self):
        inp = '''1'''
        fmt = '''(1B3.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_75(self):
        inp = '''-1'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_76(self):
        inp = '''2'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_77(self):
        inp = '''10'''
        fmt = '''(1B3.3)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_78(self):
        inp = '''-10'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_79(self):
        inp = '''100'''
        fmt = '''(1B3.3)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_80(self):
        inp = '''-100'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_81(self):
        inp = '''1000'''
        fmt = '''(1B3.3)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_82(self):
        inp = '''-1000'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_83(self):
        inp = '''10000'''
        fmt = '''(1B3.3)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_84(self):
        inp = '''-10000'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_85(self):
        inp = '''100000'''
        fmt = '''(1B3.3)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_86(self):
        inp = '''-100000'''
        fmt = '''(1B3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_87(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B3.3)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_88(self):
        inp = '''10101000'''
        fmt = '''(1B3.3)'''
        result = [5]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_89(self):
        inp = '''0'''
        fmt = '''(1B5.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_90(self):
        inp = '''-0'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_91(self):
        inp = '''1'''
        fmt = '''(1B5.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_92(self):
        inp = '''-1'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_93(self):
        inp = '''2'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_94(self):
        inp = '''10'''
        fmt = '''(1B5.3)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_95(self):
        inp = '''-10'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_96(self):
        inp = '''100'''
        fmt = '''(1B5.3)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_97(self):
        inp = '''-100'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_98(self):
        inp = '''1000'''
        fmt = '''(1B5.3)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_99(self):
        inp = '''-1000'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_100(self):
        inp = '''10000'''
        fmt = '''(1B5.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_101(self):
        inp = '''-10000'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_102(self):
        inp = '''100000'''
        fmt = '''(1B5.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_103(self):
        inp = '''-100000'''
        fmt = '''(1B5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_104(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B5.3)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_105(self):
        inp = '''10101000'''
        fmt = '''(1B5.3)'''
        result = [21]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_106(self):
        inp = '''0'''
        fmt = '''(1B10.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_107(self):
        inp = '''-0'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_108(self):
        inp = '''1'''
        fmt = '''(1B10.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_109(self):
        inp = '''-1'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_110(self):
        inp = '''2'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_111(self):
        inp = '''10'''
        fmt = '''(1B10.3)'''
        result = [2]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_112(self):
        inp = '''-10'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_113(self):
        inp = '''100'''
        fmt = '''(1B10.3)'''
        result = [4]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_114(self):
        inp = '''-100'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_115(self):
        inp = '''1000'''
        fmt = '''(1B10.3)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_116(self):
        inp = '''-1000'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_117(self):
        inp = '''10000'''
        fmt = '''(1B10.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_118(self):
        inp = '''-10000'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_119(self):
        inp = '''100000'''
        fmt = '''(1B10.3)'''
        result = [32]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_120(self):
        inp = '''-100000'''
        fmt = '''(1B10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='B')
    def test_b_ed_input_121(self):
        inp = '''10 0 00 10  0 0 1'''
        fmt = '''(1B10.3)'''
        result = [66]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()
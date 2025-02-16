# Changelog

## V 1.2.2

- Bug: [Issue 28](https://github.com/brendanarnold/py-fortranformat/issues/28) Fix a bug where crash occurs on outputting infinity or NaN for a floating point number type.

## V 1.2.1

- Feature: [Issue 25](https://github.com/brendanarnold/py-fortranformat/issues/25) Include a minimal test suite for use where resources are limited e.g. pipeline builds

## V 1.2.0

- Bug: [Issue 21](https://github.com/brendanarnold/py-fortranformat/issues/21) Now outputs FORTRAN default values when `None` is passed.

## V 1.1.1

- Bug: [Issue 15](https://github.com/brendanarnold/py-fortranformat/issues/15) Fix hanging when no suitable edit descriptor specified for `G_INPUT_TRIAL_EDS`. Now raises `ValueError`

## V 1.1.0

- Bug: Fixed overflow behaviour in tests, in particular fixing the PROC_MAXINT behaviour
- Bug: [Issue 17](https://github.com/brendanarnold/py-fortranformat/issues/17) Properly outputs zero dp floating point numbers
- Migrated to development on Python 3 (non-test code still compatible with Python 2)
- Generally used more standard project structure as detailed at [https://docs.python-guide.org/writing/structure/](https://docs.python-guide.org/writing/structure/)

## V 1.0.1

- Bug: Incorrect case on filename prevented `setup.py` executing on case-sensitive filesystems

## V 1.0.0

- **BREAKING** No longer uses `eval` for importing modules - `eval` was originally used to support very early versions of Python (2.3+) but it now means that modern packaging systems cannot understand `fortranformat` module structure. Since the latter is a more likely use-case the `eval` statements have now been dropped. It has been tested with Python 2.7+ and likely still works with earlier versions
- Migrated and recreated docs on Git/Github from Mercurial/Bitbucket
- Fixed issue where decimal values of G and E edit descriptors were causing exceptions on output
- The `config.RECORD_SEPARATOR` is not reset properly when calling `config.reset()`
- Tests for more of the edge cases
- Edit descriptors now output quoted strings even when there are no more values to output

## V 0.2.3

- Fixed issue 10 - Edit descriptor reversion now starts a new record

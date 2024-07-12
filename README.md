[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

# NO LONGER MAINTAINED

> [!IMPORTANT]
> Since the launch of Kaia Blockchain this repository has been parked in favour of the new open-source projects in [Kaia's Github](https://github.com/kaiachain). Contributors have now moved there continuing with massive open-source contributions to our blockchain ecosystem. A big thank you to everyone who has contributed to this repository.
>
> For future development and contributions, please refer to the new [kaia-core-tests repository](https://github.com/kaiachain/kaia-core-tests).
>
> For more information about Klaytn's chain merge with Finschia blockchain please refer to the launching of Kaia blockchain - [kaia.io](https://kaia.io/).

---

Klaytn tests
============

Common tests for Klaytn clients.


Documentation
-------------

You can build the documents html under `docs` directory:

```
$ make html
```

Since this test suite is ported from https://github.com/ethereum/tests, you can
also refer to Ethereum's documentation http://ethereum-tests.readthedocs.io/
although the content may not be the same.


Contents of this repository
---------------------------

Test files in the folders below are currently used for testing:
* BlockchainTests
* GeneralStateTests
* RLPTests
* TransactionTests 
* VMTests

NOTE: Originally BlockchainTests, GeneralStateTests, TransactionTests, and VMTests
were created by the testFillers which could be found at
https://github.com/ethereum/cpp-ethereum/tree/develop/test/tools/jsontests at
src folder.  However, Klaytn tests currently cannot use the testFillers.  We
will make our own filler specification and testFillers.


How to use test set
-------------------

To use this test set, you need to clone this repository or make a symbolic link
inside `tests` of https://github.com/klaytn/klaytn/ as `testdata`.
For details, see https://github.com/klaytn/klaytn/blob/master/tests/README.md.


Test set sanitation
-------------------

NOTE: The content in this section may not be valid.

### Format

All files should be of the form:

```
{
	"test1name":
	{
		"test1property1": ...,
		"test1property2": ...,
		...
	},
	"test2name":
	{
		"test2property1": ...,
		"test2property2": ...,
		...
	}
}
```

Arrays are allowed, but don't use them for sets of properties - only use them
for data that is clearly a continuous contiguous sequence of values.

### Checkers

Several basic checks against the test-set are performed to ensure that they
have been filled and are formatted correctly.  Currently, there are three types
of checks that we can perform:

- `make TEST_PREFIX.format`: check that the JSON is formatted correctly.
- `make TEST_PREFIX.valid`: check that the JSON files are valid against the
  JSON schemas in `./JSONSchema`.
- `make TEST_PREFIX.filled`: check that the JSON tests are filled with the
  correct source hashes against the fillers.

The constant `TEST_PREFIX` is a path prefix to the test-set you're interested
in performing the checks on.  For instance:

- `make ./src/VMTestsFiller/vmArithmeticTest.format` will check that all JSON
  files in `./src/VMTestsFiller/vmArithmeticTest` are formatted correctly.
- `make ./src.valid` will check that all the JSON files in `./src` are valid
  against the JSON schemas in `./JSONSchema`.
- `make ./BlockchainTests.filled` will check that the source hashes in the JSON
  tests in `./BlockchainTests` are the same as the hashes of the fillers in
  `./src/BlockchainTestsFiller`.

These checks are all performed by the file `./test.py`, which can be invoked on
individual files as well.  Run `./test.py` with no arguments for help.

### Sanitizers

The above checkers are packaged together into sanitizers for each test-suite,
marking which testsuites are passing which testers.
See the `TODO`s in the `Makefile` to see which checkers are enabled for which test-suites.

- `make sani`: will run all passing sanitizers on all passing testsuites.
- `make sani-TESTNAME`: will run just the passing sanitizers for the given testsuite.
  `TESTNAME` can be one of:

    - `vm`: VMTests and VMTestsFiller
    - `gs`: GeneralStateTests and GeneralStateTestsFiller
    - `bc`: BlockchainTests and BlockchainTestsFiller
    - `tx`: TransactionTests and TransactionTestsFiller


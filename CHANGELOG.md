## 0.1.0 (2025-05-22)


### Features
* Add support for Nuke 16 (#219) ([`f1fc0a1`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/f1fc0a12bea583688064aff301a1400ab1bb965f))
* **adaptor**: Update Nuke environment variable to NUKE_EXECUTABLE (#178) ([`4af4fff`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/4af4fffa61a170f1dc2e1ea364f4a75ff43d32d4))
* Handle different OCIO configs in adapter (#168) ([`5d55675`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/5d55675eab8e17155eb7a5044f9453b473700fb4))
* Added support for including gizmos in job bundle (#162) ([`a0704a3`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/a0704a359d4e83daade6bf41b1b766886384c37d))
* add ability to configure timeouts in submission UI (#143) ([`4535fa0`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/4535fa0a9bbd9a05ca1dd204da70e02f62b7c033))
* public release (#123) ([`515891b`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/515891bec7f82da0e8efaab2e6f94adf1a7289b7))
* Improve telemetry for submitter and adaptor (#103) ([`0811e05`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/0811e0500547326ef9b3d369f1aa3211073c5616))
* **deps**: update openjd-adaptor-runtime to 0.5 (#100) ([`b01e7f5`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/b01e7f5a2bdcc0b18a39d63737067143b5a126e2))
* Create a script to build adaptor package artifacts (#85) ([`0039d36`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/0039d3607caa0a441d8f12cd3dd5687f26fb1c02))
* detect modified files before submission and warn user. (#58) ([`ebf0100`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/ebf010043ac8c2718fdcd8e0beca73f948fe480c))
* [Nuke] Added MOV support (#46) ([`7158802`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/7158802a54c477d0e60bc17dde12929002b96678))
* Adding telemetry events for adaptor and submitter actions (#44) ([`6ecd0b6`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/6ecd0b6cf8196cb75febaaf61b7c4c0051140a14))
* **submitter**: Enable capability UI for Nuke Submitter (#36) ([`307370c`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/307370c2fc2e5f0234dcc1cc9a2cb1f16605626e))
* Apply path mapping for OCIO configs with absolute search paths (#34) ([`93fa922`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/93fa922f7abec3f1e1ec367d6dcccf65d27b032d))
* Add custom OCIO config to job attachments when enabled (#16) ([`df01abc`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/df01abcee93a2d734680e71061322f8a44bb61ec))
* update to the 2023-09 job template schema (#4) ([`8e6b8c1`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/8e6b8c1e97c1b86c356e82b1e716cb4be1275028))

### Bug Fixes
* test release notes ([`a8d12fc`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/a8d12fcc4606451310b8eb0d6e27717f5f622f2f))
* Add Windows support to GitHub Actions and skip OCIO tests on Win… (#217) ([`2296179`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/229617933bc9dc3e4ba93b249b264b145a81c5b1))
* update test_installer.sh permissions to 755 (#215) ([`5bd1a70`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/5bd1a7000527c7ac080c2ac766a3892ae1e40674))
* maintain backward compatibility with NUKE_ADAPTOR_NUKE_EXECUTABLE (#213) ([`eeb1390`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/eeb13906c7923dfe546196dccf2d9326c86d7def))
* update changelog template to use correct element keys (#212) ([`561b825`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/561b825da5494135aa639a2e6068fffe963f7b60))
* add continue on error option to submitter UI (#208) ([`0e1bdb2`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/0e1bdb267079081e643a7a96c8813235b1907d47))
* Update UI labels to use consistent sentence case (#205) ([`8e02246`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/8e02246ec4cb573eb9bd3d3d93cc0153938e54fd))
* Resolve menu.py not found error when installing via pip (#172) ([`9364964`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/9364964e50b02cda097df3866fa6c7bc755d7878))
* Revert "fix: Resolve menu.py not found error when running pip install deadline-cloud-for-nuke -t <folder> (#165)" (#170) ([`71b8c8b`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/71b8c8b762f7f3a1999640a4e6a3d646e575146d))
* Add OCIO configuration to Job Environments (#166) ([`0eb87cb`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/0eb87cbdb1bf86dff2799b48ba4ef89c70341c21))
* Resolve menu.py not found error when running pip install deadline-cloud-for-nuke -t <folder> (#165) ([`82b7eb2`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/82b7eb2d9f509a09c9974ec237a1031f4782847a))
* Update frame range when write node is selected (#161) ([`e6398c9`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/e6398c919ae7faa099f007ad2195732958ac0f9a))
* update frame range when write node is selected (#154) ([`fd4afb1`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/fd4afb173a7436cfb2ed00b4b03d09291369a141))
* Update write nodes and views when refeshing the job settings ui (#151) ([`1175cc9`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/1175cc9c4d71bbaeec49d707f40058feb6dba4f9))
* include adaptor wheels developer option (#142) ([`0edc735`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/0edc735b2a2f117abddb43d9fc5cfdd013c315f1))
* check for movie output regardless of adaptor override (#134) ([`0fda9a7`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/0fda9a75338fa30bbe4125bab503b8a6654e7d4f))
* show the correct supported versions (#129) ([`d2e5774`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/d2e577419269cce3d3c5c3db19423682e57a36bc))
* include deps with openjd adaptor package (#121) ([`fed5129`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/fed5129a936522b26bc34d955b03f4d6ccf1387a))
* include the adaptor deps in the package (#119) ([`ca51be5`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/ca51be5de62d5de1e5c851ce769473be3dacd17b))
* incorrect package name in create adaptor script (#120) ([`ba2f9f8`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/ba2f9f8a37839c382bb19dfadfb548028022c578))
* include deadline-cloud in the adaptor packaging script (#117) ([`9a72baf`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/9a72baff204d2073c35fdede2dc238c2e6515ee0))
* include description on submission (#89) ([`13b4a56`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/13b4a56a263d55ef1277711bca8e9a01db78a83a))
* prevent menu clash with Deadline10 (#86) ([`d5f3d12`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/d5f3d128b1eed20997959aef6b5f5cb5c9fb0f42))
* use right mode when opening toml file (#83) ([`7097cf3`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/7097cf37ff71ee23bb054348d7a4967c17255c5f))
* libtoml -> tomllib in depsBundle.py (#82) ([`70b3eaf`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/70b3eafff63722232d9568ff4d8ad1f6b3a7f58f))
* submitter should stay on top of main Nuke window, like all other child windows. (#59) ([`500a42e`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/500a42e821d235484c7975dc4ba39b999b25009e))
* Add default rezPackages + updated deadline dependency to 0.32 (#48) ([`d40bc5e`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/d40bc5e9c3ac5d9d3b9ca825e785a62e6f7c40b2))
* Fix job bundle tests for Mac (#40) ([`9396bac`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/9396bacb51eb454c42842d2b306c50bf8f98584f))
* Include nuke_util dir in installer (#41) ([`94a6de0`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/94a6de08abeeb7836dc2d1eb13babc820f2cdebd))
* check for modified script file and recurse group nodes for asset references (#39) ([`20911bc`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/20911bc2987b598739579a763159fe1b0d32192c))
* Mock DeadlineCredentialsStatus.getInstance call in tests (#38) ([`5a5bbe5`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/5a5bbe5483ce8e1863dac7d9aaf486c7679f1ed2))
* rename deadline.nuke to deadline.nuke_util (#37) ([`e8ba2f7`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/e8ba2f7084d509005ce879ff16e1a09ff30bdfd2))
* Support for exporting bundle with selected Write node (#32) ([`2fd0dea`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/2fd0deaa6e6c28108b17f187b510b2fb45588b9b))
* Move from openjd to openjd-adaptor-runtime (#31) ([`bd4782a`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/bd4782a0169d3aaae76ab3e91019543f790edb96))
* support spaces in the adaptor override paths (#30) ([`fbd39fb`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/fbd39fb715460885c7e2d001ea5aa12e35da6cd9))
* rename install builder components to match other submitters (#27) ([`2b0d820`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/2b0d82092f1ddb9d9455b99c742151e0520a6392))
* Handle case when the Deadline Cloud Submitter is opened from an unsaved scene ([`f660fdf`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/f660fdf7a63cc8d57c6af45583478ae3787f0c9e))
* minor changes and fixing typos ([`1fcdec4`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/1fcdec481899d7c9c7708167001444d63e21711c))
* adaptor wheel error dialog and unit test coverage ([`d8dbbe5`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/d8dbbe5fdf165c70a3f99cdb1a6680686e2e0699))
* job fails if Write node has no folders in filename (#14) ([`294f150`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/294f150c341d668970ad203ec4bb27650d602b2a))
* startfile mock on non-win platforms ([`aeb5162`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/aeb51621284bf41c943f5958a50c6e1e162a42b2))
* Update the rez package name from deadline_nuke to deadline_cloud_for_nuke (#7) ([`e7abfb5`](https://github.com/moorec-aws/deadline-cloud-for-nuke/commit/e7abfb5c007aa937287906eefde853e0b14130a7))

## 0.18.10 (2025-05-17)


### Features
* Add support for Nuke 16 (#219) ([`f1fc0a1`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/f1fc0a12bea583688064aff301a1400ab1bb965f))


## 0.18.9 (2025-04-14)


### Features
* **adaptor**: Update Nuke environment variable to NUKE_EXECUTABLE (#178) ([`4af4fff`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/4af4fffa61a170f1dc2e1ea364f4a75ff43d32d4))
* Nuke individual installer setup (#206) ([`f6ce5d7`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/f6ce5d7c6882333557d41db4adc451c9283355c9))

### Bug Fixes
* Add Windows support to GitHub Actions and skip OCIO tests on Win… (#217) ([`2296179`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/229617933bc9dc3e4ba93b249b264b145a81c5b1))
* update test_installer.sh permissions to 755 (#215) ([`5bd1a70`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/5bd1a7000527c7ac080c2ac766a3892ae1e40674))
* Fix individual installer build process (#210) ([`3167647`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/31676473833a41ced78145b5ef95d94f380e616b))
* maintain backward compatibility with NUKE_ADAPTOR_NUKE_EXECUTABLE (#213) ([`eeb1390`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/eeb13906c7923dfe546196dccf2d9326c86d7def))
* update changelog template to use correct element keys (#212) ([`561b825`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/561b825da5494135aa639a2e6068fffe963f7b60))
* add continue on error option to submitter UI (#208) ([`0e1bdb2`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/0e1bdb267079081e643a7a96c8813235b1907d47))
* Update UI labels to use consistent sentence case (#205) ([`8e02246`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/8e02246ec4cb573eb9bd3d3d93cc0153938e54fd))

## 0.18.8 (2024-11-27)

### Bug Fixes
* Revert &#34;fix: Resolve menu.py not found error when installing via pip (#172)&#34; (#175)([`3d3a8e9`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/3d3a8e9b3acc77988c0967744d8031ebb12509c1))



## 0.18.7 (2024-11-21)



### Bug Fixes
* Resolve menu.py not found error when installing via pip (#172) ([`9364964`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/9364964e50b02cda097df3866fa6c7bc755d7878))

## 0.18.6 (2024-10-21)



### Bug Fixes
* Revert &#34;fix: Resolve menu.py not found error when running pip install deadline-cloud-for-nuke -t &lt;folder&gt; (#165)&#34; (#170) ([`71b8c8b`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/71b8c8b762f7f3a1999640a4e6a3d646e575146d))

## 0.18.5 (2024-10-16)


### Features
* Handle different OCIO configs in adapter (#168) ([`5d55675`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/5d55675eab8e17155eb7a5044f9453b473700fb4))
* Added support for including gizmos in job bundle (#162) ([`a0704a3`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/a0704a359d4e83daade6bf41b1b766886384c37d))

### Bug Fixes
* Add OCIO configuration to Job Environments (#166) ([`0eb87cb`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/0eb87cbdb1bf86dff2799b48ba4ef89c70341c21))
* Resolve menu.py not found error when running pip install deadline-cloud-for-nuke -t &lt;folder&gt; (#165) ([`82b7eb2`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/82b7eb2d9f509a09c9974ec237a1031f4782847a))
* Update frame range when write node is selected (#161) ([`e6398c9`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/e6398c919ae7faa099f007ad2195732958ac0f9a))

## 0.18.4 (2024-08-12)



### Bug Fixes
* Update write nodes and views when refeshing the job settings ui (#151) ([`1175cc9`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/1175cc9c4d71bbaeec49d707f40058feb6dba4f9))

## 0.18.3 (2024-05-29)


### Features
* add ability to configure timeouts in submission UI (#143) ([`4535fa0`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/4535fa0a9bbd9a05ca1dd204da70e02f62b7c033))

### Bug Fixes
* include adaptor wheels developer option (#142) ([`0edc735`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/0edc735b2a2f117abddb43d9fc5cfdd013c315f1))

## 0.18.2 (2024-05-01)



### Bug Fixes
* check for movie output regardless of adaptor override (#134) ([`0fda9a7`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/0fda9a75338fa30bbe4125bab503b8a6654e7d4f))

## 0.18.1 (2024-04-02)



### Bug Fixes
* show the correct supported versions (#129) ([`d2e5774`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/d2e577419269cce3d3c5c3db19423682e57a36bc))

## 0.18.0 (2024-04-01)

### BREAKING CHANGES
* public release (#123) ([`515891b`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/515891bec7f82da0e8efaab2e6f94adf1a7289b7))


### Bug Fixes
* include deps with openjd adaptor package (#121) ([`fed5129`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/fed5129a936522b26bc34d955b03f4d6ccf1387a))
* include the adaptor deps in the package (#119) ([`ca51be5`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/ca51be5de62d5de1e5c851ce769473be3dacd17b))
* incorrect package name in create adaptor script (#120) ([`ba2f9f8`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/ba2f9f8a37839c382bb19dfadfb548028022c578))
* set python 3.8 to minimum python version in hatch testing matrix (#123) ([`515891b`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/515891bec7f82da0e8efaab2e6f94adf1a7289b7))

## 0.17.2 (2024-03-26)


### Features
* Improve telemetry for submitter and adaptor (#103) ([`0811e05`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/0811e0500547326ef9b3d369f1aa3211073c5616))

### Bug Fixes
* include deadline-cloud in the adaptor packaging script (#117) ([`9a72baf`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/9a72baff204d2073c35fdede2dc238c2e6515ee0))

## 0.17.1 (2024-03-15)

### Chore
* update deps deadline-cloud 0.40 (#107) ([`6503f29`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/6503f293c9f9ea7be5a513d84dffd4d4f0c2dc5f))


## 0.17.0 (2024-03-08)

### BREAKING CHANGES
* **deps**: update openjd-adaptor-runtime to 0.5 (#100) ([`b01e7f5`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/b01e7f5a2bdcc0b18a39d63737067143b5a126e2))



## 0.16.0 (2024-02-21)

### BREAKING CHANGES
* Create a script to build adaptor package artifacts (#85) ([`0039d36`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/0039d3607caa0a441d8f12cd3dd5687f26fb1c02))


### Bug Fixes
* include description on submission (#89) ([`13b4a56`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/13b4a56a263d55ef1277711bca8e9a01db78a83a))
* prevent menu clash with Deadline10 (#86) ([`d5f3d12`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/d5f3d128b1eed20997959aef6b5f5cb5c9fb0f42))
* use right mode when opening toml file (#83) ([`7097cf3`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/7097cf37ff71ee23bb054348d7a4967c17255c5f))
* libtoml -&gt; tomllib in depsBundle.py (#82) ([`70b3eaf`](https://github.com/aws-deadline/deadline-cloud-for-nuke/commit/70b3eafff63722232d9568ff4d8ad1f6b3a7f58f))


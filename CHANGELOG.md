# CHANGELOG



## v0.8.0 (2024-02-02)

### Chore

* chore(deps-dev): Bump pytest from 7.4.4 to 8.0.0 (#167) ([`ed3ad69`](https://github.com/Nr18/cfn-guard-test/commit/ed3ad69e7e497fc9770afda909309640d1d06005))

* chore(deps-dev): Bump black from 24.1.0 to 24.1.1 (#166)

Bumps [black](https://github.com/psf/black) from 24.1.0 to 24.1.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.1.1&lt;/h2&gt;
&lt;p&gt;Bugfix release to fix a bug that made Black unusable on certain file
systems
with strict limits on path length.&lt;/p&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently add trailing comma on typed parameters (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4164&#34;&gt;#4164&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Shorten the length of the name of the cache file to fix crashes on
file systems that
do not support long paths (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4176&#34;&gt;#4176&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.1.1&lt;/h2&gt;
&lt;p&gt;Bugfix release to fix a bug that made Black unusable on certain file
systems with strict
limits on path length.&lt;/p&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently add trailing comma on typed parameters (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4164&#34;&gt;#4164&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Shorten the length of the name of the cache file to fix crashes on
file systems that
do not support long paths (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4176&#34;&gt;#4176&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e026c93888f91a47a9c9f4e029f3eb07d96375e6&#34;&gt;&lt;code&gt;e026c93&lt;/code&gt;&lt;/a&gt;
Prepare release 24.1.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4186&#34;&gt;#4186&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/79fc1158a98281dac798feb14b8fddb4051e4a42&#34;&gt;&lt;code&gt;79fc115&lt;/code&gt;&lt;/a&gt;
chore: ignore node_modules (produced by a pre-commit check) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4184&#34;&gt;#4184&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8bf04549ffd276a1bad6eb110e66e6557ee630d9&#34;&gt;&lt;code&gt;8bf0454&lt;/code&gt;&lt;/a&gt;
Consistently add trailing comma on typed parameters (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4164&#34;&gt;#4164&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1607e9ab20ad550cf940482d0d361ca31fc03189&#34;&gt;&lt;code&gt;1607e9a&lt;/code&gt;&lt;/a&gt;
Fix missing space in option description (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4182&#34;&gt;#4182&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ed770ba4dd50c419148a0fca2b43937a7447e1f9&#34;&gt;&lt;code&gt;ed770ba&lt;/code&gt;&lt;/a&gt;
Fix cache file length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4176&#34;&gt;#4176&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/659c29a41c7c686687aef21f57b95bcfa236b03b&#34;&gt;&lt;code&gt;659c29a&lt;/code&gt;&lt;/a&gt;
New changelog&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/psf/black/compare/24.1.0...24.1.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=24.1.0&amp;new-version=24.1.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`4182391`](https://github.com/Nr18/cfn-guard-test/commit/4182391c210648e47ce050e7ba2f66cf12e05cc9))

* chore(deps-dev): Bump black from 23.12.1 to 24.1.0 (#165) ([`122833e`](https://github.com/Nr18/cfn-guard-test/commit/122833eefab5531ea901fcb64b38032694143f1a))

* chore(deps-dev): Bump jinja2 from 3.1.2 to 3.1.3 (#164)

Bumps [jinja2](https://github.com/pallets/jinja) from 3.1.2 to 3.1.3.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/jinja/releases&#34;&gt;jinja2&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;3.1.3&lt;/h2&gt;
&lt;p&gt;This is a fix release for the 3.1.x feature branch.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fix for &lt;a
href=&#34;https://github.com/pallets/jinja/security/advisories/GHSA-h5c8-rqwp-cp95&#34;&gt;GHSA-h5c8-rqwp-cp95&lt;/a&gt;.
You are affected if you are using &lt;code&gt;xmlattr&lt;/code&gt; and passing user
input as attribute keys.&lt;/li&gt;
&lt;li&gt;Changes: &lt;a
href=&#34;https://jinja.palletsprojects.com/en/3.1.x/changes/#version-3-1-3&#34;&gt;https://jinja.palletsprojects.com/en/3.1.x/changes/#version-3-1-3&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Milestone: &lt;a
href=&#34;https://github.com/pallets/jinja/milestone/15?closed=1&#34;&gt;https://github.com/pallets/jinja/milestone/15?closed=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/jinja/blob/main/CHANGES.rst&#34;&gt;jinja2&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;Version 3.1.3&lt;/h2&gt;
&lt;p&gt;Released 2024-01-10&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fix compiler error when checking if required blocks in parent
templates are
empty. :pr:&lt;code&gt;1858&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;xmlattr&lt;/code&gt; filter does not allow keys with spaces.
GHSA-h5c8-rqwp-cp95&lt;/li&gt;
&lt;li&gt;Make error messages stemming from invalid nesting of &lt;code&gt;{% trans
%}&lt;/code&gt; blocks
more helpful. :pr:&lt;code&gt;1918&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/d9de4bb215fd1cc8092a410fb834c7c4060b1fc1&#34;&gt;&lt;code&gt;d9de4bb&lt;/code&gt;&lt;/a&gt;
release version 3.1.3&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/50124e16561f17f6c1ec85a692f6551418971cdc&#34;&gt;&lt;code&gt;50124e1&lt;/code&gt;&lt;/a&gt;
skip test pypi&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/9ea7222ef3f184480be0d0884e30ccfb4172b17b&#34;&gt;&lt;code&gt;9ea7222&lt;/code&gt;&lt;/a&gt;
use trusted publishing&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/da703f7aae36b1e88baaa20de334d7ff6378fdde&#34;&gt;&lt;code&gt;da703f7&lt;/code&gt;&lt;/a&gt;
use trusted publishing&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/bce174692547464512383ec40e0f8338b8811983&#34;&gt;&lt;code&gt;bce1746&lt;/code&gt;&lt;/a&gt;
use trusted publishing&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/7277d8068be593deab3555c7c14f974ada373af1&#34;&gt;&lt;code&gt;7277d80&lt;/code&gt;&lt;/a&gt;
update pre-commit hooks&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/5c8a10522421270f66376a24ec8e0d6812bc4b14&#34;&gt;&lt;code&gt;5c8a105&lt;/code&gt;&lt;/a&gt;
Make nested-trans-block exceptions nicer (&lt;a
href=&#34;https://redirect.github.com/pallets/jinja/issues/1918&#34;&gt;#1918&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/19a55db3b411343309f2faaffaedbb089e841895&#34;&gt;&lt;code&gt;19a55db&lt;/code&gt;&lt;/a&gt;
Make nested-trans-block exceptions nicer&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/716795349a41d4983a9a4771f7d883c96ea17be7&#34;&gt;&lt;code&gt;7167953&lt;/code&gt;&lt;/a&gt;
Merge pull request from GHSA-h5c8-rqwp-cp95&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/jinja/commit/7dd3680e6eea0d77fde024763657aa4d884ddb23&#34;&gt;&lt;code&gt;7dd3680&lt;/code&gt;&lt;/a&gt;
xmlattr filter disallows keys with spaces&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pallets/jinja/compare/3.1.2...3.1.3&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=jinja2&amp;package-manager=pip&amp;previous-version=3.1.2&amp;new-version=3.1.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/cfn-guard-test/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`ce896c3`](https://github.com/Nr18/cfn-guard-test/commit/ce896c3df4368e0a4c6b98b80ddd7802f1fbdecd))

* chore(deps-dev): Bump gitpython from 3.1.37 to 3.1.41 (#163)

Bumps [gitpython](https://github.com/gitpython-developers/GitPython)
from 3.1.37 to 3.1.41.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/releases&#34;&gt;gitpython&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;3.1.41 - fix Windows security issue&lt;/h2&gt;
&lt;p&gt;The details about the Windows security issue &lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/security/advisories/GHSA-2mqj-m65w-jghx&#34;&gt;can
be found in this advisory&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Special thanks go to &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; who
reported the issue and fixed it in a single stroke, while being
responsible for an incredible amount of improvements that he contributed
over the last couple of months ❤️.&lt;/p&gt;
&lt;h2&gt;What&#39;s Changed&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;Add &lt;code&gt;__all__&lt;/code&gt; in git.exc by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1719&#34;&gt;gitpython-developers/GitPython#1719&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Set submodule update cadence to weekly by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1721&#34;&gt;gitpython-developers/GitPython#1721&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Never modify sys.path by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1720&#34;&gt;gitpython-developers/GitPython#1720&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Bump git/ext/gitdb from &lt;code&gt;8ec2390&lt;/code&gt; to &lt;code&gt;ec58b7e&lt;/code&gt;
by &lt;a href=&#34;https://github.com/dependabot&#34;&gt;&lt;code&gt;@​dependabot&lt;/code&gt;&lt;/a&gt;
in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1722&#34;&gt;gitpython-developers/GitPython#1722&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Revise comments, docstrings, some messages, and a bit of code by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1725&#34;&gt;gitpython-developers/GitPython#1725&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Use zero-argument super() by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1726&#34;&gt;gitpython-developers/GitPython#1726&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Remove obsolete note in _iter_packed_refs by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1727&#34;&gt;gitpython-developers/GitPython#1727&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Reorganize test_util and make xfail marks precise by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1729&#34;&gt;gitpython-developers/GitPython#1729&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Clarify license and make module top comments more consistent by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1730&#34;&gt;gitpython-developers/GitPython#1730&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Deprecate compat.is_&lt;!-- raw HTML omitted --&gt;, rewriting all uses by
&lt;a href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in
&lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1732&#34;&gt;gitpython-developers/GitPython#1732&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Revise and restore some module docstrings by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1735&#34;&gt;gitpython-developers/GitPython#1735&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Make the rmtree callback Windows-only by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1739&#34;&gt;gitpython-developers/GitPython#1739&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;List all non-passing tests in test summaries by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1740&#34;&gt;gitpython-developers/GitPython#1740&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Document some minor subtleties in test_util.py by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1749&#34;&gt;gitpython-developers/GitPython#1749&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Always read metadata files as UTF-8 in setup.py by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1748&#34;&gt;gitpython-developers/GitPython#1748&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Test native Windows on CI by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1745&#34;&gt;gitpython-developers/GitPython#1745&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Test macOS on CI by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1752&#34;&gt;gitpython-developers/GitPython#1752&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Let close_fds be True on all platforms by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1753&#34;&gt;gitpython-developers/GitPython#1753&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Fix IndexFile.from_tree on Windows by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1751&#34;&gt;gitpython-developers/GitPython#1751&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Remove unused TASKKILL fallback in AutoInterrupt by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1754&#34;&gt;gitpython-developers/GitPython#1754&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Don&#39;t return with operand when conceptually void by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1755&#34;&gt;gitpython-developers/GitPython#1755&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Group .gitignore entries by purpose by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1758&#34;&gt;gitpython-developers/GitPython#1758&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Adding dubious ownership handling by &lt;a
href=&#34;https://github.com/marioaag&#34;&gt;&lt;code&gt;@​marioaag&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1746&#34;&gt;gitpython-developers/GitPython#1746&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Avoid brittle assumptions about preexisting temporary files in tests
by &lt;a href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt;
in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1759&#34;&gt;gitpython-developers/GitPython#1759&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Overhaul noqa directives by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1760&#34;&gt;gitpython-developers/GitPython#1760&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Clarify some Git.execute kill_after_timeout limitations by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1761&#34;&gt;gitpython-developers/GitPython#1761&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Bump actions/setup-python from 4 to 5 by &lt;a
href=&#34;https://github.com/dependabot&#34;&gt;&lt;code&gt;@​dependabot&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1763&#34;&gt;gitpython-developers/GitPython#1763&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Don&#39;t install black on Cygwin by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1766&#34;&gt;gitpython-developers/GitPython#1766&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Extract all &amp;quot;import gc&amp;quot; to module level by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1765&#34;&gt;gitpython-developers/GitPython#1765&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Extract remaining local &amp;quot;import gc&amp;quot; to module level by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1768&#34;&gt;gitpython-developers/GitPython#1768&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Replace xfail with gc.collect in TestSubmodule.test_rename by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1767&#34;&gt;gitpython-developers/GitPython#1767&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Enable CodeQL by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1769&#34;&gt;gitpython-developers/GitPython#1769&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Replace some uses of the deprecated mktemp function by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1770&#34;&gt;gitpython-developers/GitPython#1770&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Bump github/codeql-action from 2 to 3 by &lt;a
href=&#34;https://github.com/dependabot&#34;&gt;&lt;code&gt;@​dependabot&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1773&#34;&gt;gitpython-developers/GitPython#1773&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Run some Windows environment variable tests only on Windows by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1774&#34;&gt;gitpython-developers/GitPython#1774&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Fix TemporaryFileSwap regression where file_path could not be Path
by &lt;a href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt;
in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1776&#34;&gt;gitpython-developers/GitPython#1776&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Improve hooks tests by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1777&#34;&gt;gitpython-developers/GitPython#1777&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Fix if items of Index is of type PathLike by &lt;a
href=&#34;https://github.com/stegm&#34;&gt;&lt;code&gt;@​stegm&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1778&#34;&gt;gitpython-developers/GitPython#1778&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Better document IterableObj.iter_items and improve some subclasses
by &lt;a href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt;
in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1780&#34;&gt;gitpython-developers/GitPython#1780&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Revert &amp;quot;Don&#39;t install black on Cygwin&amp;quot; by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1783&#34;&gt;gitpython-developers/GitPython#1783&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Add missing pip in $PATH on Cygwin CI by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1784&#34;&gt;gitpython-developers/GitPython#1784&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Shorten Iterable docstrings and put IterableObj first by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1785&#34;&gt;gitpython-developers/GitPython#1785&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Fix incompletely revised Iterable/IterableObj docstrings by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1786&#34;&gt;gitpython-developers/GitPython#1786&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Pre-deprecate setting Git.USE_SHELL by &lt;a
href=&#34;https://github.com/EliahKagan&#34;&gt;&lt;code&gt;@​EliahKagan&lt;/code&gt;&lt;/a&gt; in &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/pull/1782&#34;&gt;gitpython-developers/GitPython#1782&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/f28873828496a6632b3a99101e3582ad164e9bb9&#34;&gt;&lt;code&gt;f288738&lt;/code&gt;&lt;/a&gt;
bump patch level&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/ef3192cc414f2fd9978908454f6fd95243784c7f&#34;&gt;&lt;code&gt;ef3192c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/gitpython-developers/GitPython/issues/1792&#34;&gt;#1792&lt;/a&gt;
from EliahKagan/popen&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/1f3caa31f1b63908235e341418a0804ed37a320a&#34;&gt;&lt;code&gt;1f3caa3&lt;/code&gt;&lt;/a&gt;
Further clarify comment in test_hook_uses_shell_not_from_cwd&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/3eb7c2ab82e6dbe101ff916fca29d539cc2793af&#34;&gt;&lt;code&gt;3eb7c2a&lt;/code&gt;&lt;/a&gt;
Move safer_popen from git.util to git.cmd&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/c551e916c7b9e2d623b9d76f3352849a707d9bbe&#34;&gt;&lt;code&gt;c551e91&lt;/code&gt;&lt;/a&gt;
Extract shared logic for using Popen safely on Windows&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/15ebb258d4eebd9bf0f38780570d57e0b968b8de&#34;&gt;&lt;code&gt;15ebb25&lt;/code&gt;&lt;/a&gt;
Clarify comment in test_hook_uses_shell_not_from_cwd&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/f44524a9a9c8122b9b98d6e5797e1dfc3211c0b7&#34;&gt;&lt;code&gt;f44524a&lt;/code&gt;&lt;/a&gt;
Avoid spurious &amp;quot;location may have moved&amp;quot; on Windows&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/a42ea0a38c489caf9969836141120d760d3754b4&#34;&gt;&lt;code&gt;a42ea0a&lt;/code&gt;&lt;/a&gt;
Cover absent/no-distro bash.exe in hooks &amp;quot;not from cwd&amp;quot;
test&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/7751436b94d96ce0978b301681b851edd6efed63&#34;&gt;&lt;code&gt;7751436&lt;/code&gt;&lt;/a&gt;
Extract venv management from test_installation&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/commit/66ff4c177accfb4f21d3eb476381d248d99fd8b5&#34;&gt;&lt;code&gt;66ff4c1&lt;/code&gt;&lt;/a&gt;
Omit CWD in search for bash.exe to run hooks on Windows&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/gitpython-developers/GitPython/compare/3.1.37...3.1.41&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=gitpython&amp;package-manager=pip&amp;previous-version=3.1.37&amp;new-version=3.1.41)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/cfn-guard-test/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`5bf6b2d`](https://github.com/Nr18/cfn-guard-test/commit/5bf6b2dff3d03f17bdd2b59deb1c748eb90ee080))

* chore(deps-dev): Bump pytest from 7.4.3 to 7.4.4 (#162)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.3 to
7.4.4.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;pytest 7.4.4 (2023-12-31)&lt;/h2&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11140&#34;&gt;#11140&lt;/a&gt;:
Fix non-string constants at the top of file being detected as docstrings
on Python&amp;gt;=3.8.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11572&#34;&gt;#11572&lt;/a&gt;:
Handle an edge case where &lt;code&gt;sys.stderr&lt;/code&gt;{.interpreted-text
role=&amp;quot;data&amp;quot;} and &lt;code&gt;sys.__stderr__&lt;/code&gt;{.interpreted-text
role=&amp;quot;data&amp;quot;} might already be closed when
&lt;code&gt;faulthandler&lt;/code&gt;{.interpreted-text role=&amp;quot;ref&amp;quot;} is
tearing down.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11710&#34;&gt;#11710&lt;/a&gt;:
Fixed tracebacks from collection errors not getting pruned.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/7966&#34;&gt;#7966&lt;/a&gt;:
Removed unhelpful error message from assertion rewrite mechanism when
exceptions are raised in &lt;code&gt;__iter__&lt;/code&gt; methods. Now they are
treated un-iterable instead.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Improved Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11091&#34;&gt;#11091&lt;/a&gt;:
Updated documentation to refer to hyphenated options: replaced
&lt;code&gt;--junitxml&lt;/code&gt; with &lt;code&gt;--junit-xml&lt;/code&gt; and
&lt;code&gt;--collectonly&lt;/code&gt; with &lt;code&gt;--collect-only&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/33f694f4b30c5c502f21f81cb8ab907b12ad2f65&#34;&gt;&lt;code&gt;33f694f&lt;/code&gt;&lt;/a&gt;
Prepare release version 7.4.4&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/76c107c463afcaddf74ca48252614728c6829ea7&#34;&gt;&lt;code&gt;76c107c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11751&#34;&gt;#11751&lt;/a&gt;
from bluetech/backport-11143-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/531d76daa4a871df5b2a46cae132851c29abf027&#34;&gt;&lt;code&gt;531d76d&lt;/code&gt;&lt;/a&gt;
[7.4.x] Improve reporting from &lt;strong&gt;iter&lt;/strong&gt; exceptions (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11749&#34;&gt;#11749&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a0f58fa9e7f9b09b212ed491464be5df9b80fc0b&#34;&gt;&lt;code&gt;a0f58fa&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11143&#34;&gt;#11143&lt;/a&gt;
from tushar-deepsource/patch-1&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/b1f3387d42571090ee4a35ec1945765b7f2ffae8&#34;&gt;&lt;code&gt;b1f3387&lt;/code&gt;&lt;/a&gt;
[7.4.x] &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11091&#34;&gt;#11091&lt;/a&gt;:
documentation should use hypthonated properties (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11750&#34;&gt;#11750&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/2cdd619bf49ee7c5306dc70dcbf71090839ea985&#34;&gt;&lt;code&gt;2cdd619&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11747&#34;&gt;#11747&lt;/a&gt;
from pytest-dev/backport-11711-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d06c05bd23ea6af8e07fd944e56c58b64375b724&#34;&gt;&lt;code&gt;d06c05b&lt;/code&gt;&lt;/a&gt;
[7.4.x] nodes: fix tracebacks from collection errors are not getting
pruned&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/5582bfcddf78929f7979c5023b167b333e1c2dd9&#34;&gt;&lt;code&gt;5582bfc&lt;/code&gt;&lt;/a&gt;
[7.4.x] Improves clarity in Sphinx documentation for function signature.
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11&#34;&gt;#11&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/13024efd7afdbae80ce70d27295d9bbe62670cb8&#34;&gt;&lt;code&gt;13024ef&lt;/code&gt;&lt;/a&gt;
[7.4.x] Fix for operation on closed file in faulthandler teardown (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11631&#34;&gt;#11631&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a40dacf6577ae990740e10572582538dfaf357b6&#34;&gt;&lt;code&gt;a40dacf&lt;/code&gt;&lt;/a&gt;
[7.4.x] XFAIL TestLocalPath.test_make_numbered_dir_multiprocess_safe (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11616&#34;&gt;#11616&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/7.4.3...7.4.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=7.4.3&amp;new-version=7.4.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`29329a4`](https://github.com/Nr18/cfn-guard-test/commit/29329a4be4ed8dd08cd1eec485c9767d4c2694d4))

* chore(deps-dev): Bump black from 23.12.0 to 23.12.1 (#161)

Bumps [black](https://github.com/psf/black) from 23.12.0 to 23.12.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.1&lt;/h2&gt;
&lt;p&gt;Fixed a bug that included dependencies from the d extra by default
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.1&lt;/h2&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fixed a bug that included dependencies from the &lt;code&gt;d&lt;/code&gt; extra
by default (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ec91a2be3c44d88e1a3960a4937ad6ed3b63464e&#34;&gt;&lt;code&gt;ec91a2b&lt;/code&gt;&lt;/a&gt;
Prepare release 23.12.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4124&#34;&gt;#4124&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8fec1c30855890cc9cfce5ae6d633a1c1a21d724&#34;&gt;&lt;code&gt;8fec1c3&lt;/code&gt;&lt;/a&gt;
Adds paren to deps for hidden extra constraint (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/35ce37ded7bd8fdd3950af19e7c11f311ee7b8d8&#34;&gt;&lt;code&gt;35ce37d&lt;/code&gt;&lt;/a&gt;
Add new changelog template&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/psf/black/compare/23.12.0...23.12.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.12.0&amp;new-version=23.12.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`82993e8`](https://github.com/Nr18/cfn-guard-test/commit/82993e8d8fca7dce2daccc688e05a3896716481b))

* chore(deps-dev): Bump python-semantic-release from 8.5.2 to 8.7.0 (#160)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.5.2 to 8.7.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.7.0 (2023-12-22)&lt;/h1&gt;
&lt;h2&gt;Feature&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;feat(config): enable default environment token per hvcs (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/774&#34;&gt;#774&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/26528eb8794d00dfe985812269702fbc4c4ec788&#34;&gt;&lt;code&gt;26528eb&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Style&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;style: beautify 26528eb8794d00dfe985812269702fbc4c4ec788 (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/514f5580fbec0143f88d3f637be260c769136377&#34;&gt;&lt;code&gt;514f558&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;v8.6.0 (2023-12-22)&lt;/h1&gt;
&lt;h2&gt;Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;docs: minor correction to commit-parsing documentation (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/777&#34;&gt;#777&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/245e878f02d5cafec6baf0493c921c1e396b56e8&#34;&gt;&lt;code&gt;245e878&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Feature&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;feat(utils): expand parsable valid git remote url formats (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/771&#34;&gt;#771&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Git remote url parsing now supports additional formats (ssh, https,
file, git) (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/cf75f237360488ebb0088e5b8aae626e97d9cbdd&#34;&gt;&lt;code&gt;cf75f23&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;h2&gt;Style&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;style: beautify cf75f237360488ebb0088e5b8aae626e97d9cbdd (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/2de634d6e1fed29e8ce55a1c57fd23bf838badd9&#34;&gt;&lt;code&gt;2de634d&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.7.0 (2023-12-22)&lt;/h2&gt;
&lt;h3&gt;Feature&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;feat(config): enable default environment token per hvcs (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/774&#34;&gt;#774&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/26528eb8794d00dfe985812269702fbc4c4ec788&#34;&gt;&lt;code&gt;26528eb&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;style: beautify 26528eb8794d00dfe985812269702fbc4c4ec788 (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/514f5580fbec0143f88d3f637be260c769136377&#34;&gt;&lt;code&gt;514f558&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;v8.6.0 (2023-12-22)&lt;/h2&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;docs: minor correction to commit-parsing documentation (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/777&#34;&gt;#777&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/245e878f02d5cafec6baf0493c921c1e396b56e8&#34;&gt;&lt;code&gt;245e878&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Feature&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;feat(utils): expand parsable valid git remote url formats (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/771&#34;&gt;#771&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Git remote url parsing now supports additional formats (ssh, https,
file, git) (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/cf75f237360488ebb0088e5b8aae626e97d9cbdd&#34;&gt;&lt;code&gt;cf75f23&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;h3&gt;Style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;style: beautify cf75f237360488ebb0088e5b8aae626e97d9cbdd (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/2de634d6e1fed29e8ce55a1c57fd23bf838badd9&#34;&gt;&lt;code&gt;2de634d&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/c1059f5b90895f75bde3d088bdc69e734e983535&#34;&gt;&lt;code&gt;c1059f5&lt;/code&gt;&lt;/a&gt;
8.7.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/514f5580fbec0143f88d3f637be260c769136377&#34;&gt;&lt;code&gt;514f558&lt;/code&gt;&lt;/a&gt;
style: beautify 26528eb8794d00dfe985812269702fbc4c4ec788&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/26528eb8794d00dfe985812269702fbc4c4ec788&#34;&gt;&lt;code&gt;26528eb&lt;/code&gt;&lt;/a&gt;
feat(config): enable default environment token per hvcs (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/774&#34;&gt;#774&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/38046d5e8c84443a088af6c94354ea4095c9ab70&#34;&gt;&lt;code&gt;38046d5&lt;/code&gt;&lt;/a&gt;
8.6.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/2de634d6e1fed29e8ce55a1c57fd23bf838badd9&#34;&gt;&lt;code&gt;2de634d&lt;/code&gt;&lt;/a&gt;
style: beautify cf75f237360488ebb0088e5b8aae626e97d9cbdd&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/cf75f237360488ebb0088e5b8aae626e97d9cbdd&#34;&gt;&lt;code&gt;cf75f23&lt;/code&gt;&lt;/a&gt;
feat(utils): expand parsable valid git remote url formats (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/771&#34;&gt;#771&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/245e878f02d5cafec6baf0493c921c1e396b56e8&#34;&gt;&lt;code&gt;245e878&lt;/code&gt;&lt;/a&gt;
docs: minor correction to commit-parsing documentation (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/777&#34;&gt;#777&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.5.2...v8.7.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.5.2&amp;new-version=8.7.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`03266b8`](https://github.com/Nr18/cfn-guard-test/commit/03266b86c38a993206aa9ee968881fbb06a4c591))

* chore(deps-dev): Bump mypy from 1.7.1 to 1.8.0 (#159)

Bumps [mypy](https://github.com/python/mypy) from 1.7.1 to 1.8.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python/mypy/blob/master/CHANGELOG.md&#34;&gt;mypy&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;Mypy Release Notes&lt;/h1&gt;
&lt;h2&gt;Next release&lt;/h2&gt;
&lt;h2&gt;Mypy 1.8&lt;/h2&gt;
&lt;p&gt;We’ve just uploaded mypy 1.8 to the Python Package Index (&lt;a
href=&#34;https://pypi.org/project/mypy/&#34;&gt;PyPI&lt;/a&gt;). Mypy is a static type
checker for Python. This release includes new features, performance
improvements and bug fixes. You can install it as follows:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;python3 -m pip install -U mypy
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;You can read the full documentation for this release on &lt;a
href=&#34;http://mypy.readthedocs.io&#34;&gt;Read the Docs&lt;/a&gt;.&lt;/p&gt;
&lt;h4&gt;Type-checking Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Do not intersect types in isinstance checks if at least one is final
(Christoph Tyralla, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16330&#34;&gt;16330&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Detect that &lt;code&gt;@final&lt;/code&gt; class without &lt;code&gt;__bool__&lt;/code&gt;
cannot have falsey instances (Ilya Priven, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16566&#34;&gt;16566&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Do not allow &lt;code&gt;TypedDict&lt;/code&gt; classes with extra keywords
(Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16438&#34;&gt;16438&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Do not allow class-level keywords for &lt;code&gt;NamedTuple&lt;/code&gt;
(Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16526&#34;&gt;16526&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Make imprecise constraints handling more robust (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16502&#34;&gt;16502&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix strict-optional in extending generic TypedDict (Ivan Levkivskyi,
PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16398&#34;&gt;16398&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow type ignores of PEP 695 constructs (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16608&#34;&gt;16608&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Enable &lt;code&gt;type_check_only&lt;/code&gt; support for
&lt;code&gt;TypedDict&lt;/code&gt; and &lt;code&gt;NamedTuple&lt;/code&gt; (Nikita Sobolev, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16469&#34;&gt;16469&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Performance Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Add fast path to analyzing special form assignments (Jukka
Lehtosalo, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16561&#34;&gt;16561&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Improvements to Error Reporting&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Don&#39;t show documentation links for plugin error codes (Ivan
Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16383&#34;&gt;16383&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve error messages for &lt;code&gt;super&lt;/code&gt; checks and add more
tests (Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16393&#34;&gt;16393&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add error code for mutable covariant override (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16399&#34;&gt;16399&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Stubgen Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Preserve simple defaults in function signatures (Ali Hamdan, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/15355&#34;&gt;15355&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Include &lt;code&gt;__all__&lt;/code&gt; in output (Jelle Zijlstra, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16356&#34;&gt;16356&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix stubgen regressions with pybind11 and mypy 1.7 (Chad Dombrova,
PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16504&#34;&gt;16504&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Stubtest Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Improve handling of unrepresentable defaults (Jelle Zijlstra, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16433&#34;&gt;16433&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Print more helpful errors if a function is missing from stub (Alex
Waygood, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16517&#34;&gt;16517&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Support &lt;code&gt;@type_check_only&lt;/code&gt; decorator (Nikita Sobolev, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16422&#34;&gt;16422&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Warn about missing &lt;code&gt;__del__&lt;/code&gt; (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16456&#34;&gt;16456&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crashes with some uses of &lt;code&gt;final&lt;/code&gt; and
&lt;code&gt;deprecated&lt;/code&gt; (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16457&#34;&gt;16457&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Fixes to Crashes&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash with type alias to &lt;code&gt;Callable[[Unpack[Tuple[Any,
...]]], Any]&lt;/code&gt; (Alex Waygood, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16541&#34;&gt;16541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on TypeGuard in &lt;code&gt;__call__&lt;/code&gt; (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16516&#34;&gt;16516&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on invalid enum in method (Ivan Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16511&#34;&gt;16511&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on unimported Any in TypedDict (Ivan Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16510&#34;&gt;16510&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Documentation Updates&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Update soft-error-limit default value to -1 (Sveinung Gundersen, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16542&#34;&gt;16542&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3b467509ee29b8f274c035d78a1c241a781eb311&#34;&gt;&lt;code&gt;3b46750&lt;/code&gt;&lt;/a&gt;
remove +dev suffix from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c9bc833bc8a64e3517a6843bbf982a37ee54f893&#34;&gt;&lt;code&gt;c9bc833&lt;/code&gt;&lt;/a&gt;
Fix tests broken by hatchling (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16655&#34;&gt;#16655&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/60d30e36c49a2753de2d71f7dd50f5143bafd307&#34;&gt;&lt;code&gt;60d30e3&lt;/code&gt;&lt;/a&gt;
Fix crash with type alias to &lt;code&gt;Callable[[Unpack[Tuple[Any, ...]]],
Any]&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16541&#34;&gt;#16541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f53f4222bbb12d49612657a48b4f2b77e15402fd&#34;&gt;&lt;code&gt;f53f422&lt;/code&gt;&lt;/a&gt;
Allow type ignores of PEP 695 constructs (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16608&#34;&gt;#16608&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/7c33e7c03444ae748b82163e7b4e1666dfaf94c7&#34;&gt;&lt;code&gt;7c33e7c&lt;/code&gt;&lt;/a&gt;
&lt;a href=&#34;https://github.com/final&#34;&gt;&lt;code&gt;@​final&lt;/code&gt;&lt;/a&gt; class
without &lt;strong&gt;bool&lt;/strong&gt; cannot have falsey instances (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16566&#34;&gt;#16566&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c224da5c7c414f92ded4b7816d16d5dd4ed32193&#34;&gt;&lt;code&gt;c224da5&lt;/code&gt;&lt;/a&gt;
Do not intersect types in isinstance checks if at least one is final (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16330&#34;&gt;#16330&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/d54cc35a93b1f1bda8f837e0f3ae6f964a1c7feb&#34;&gt;&lt;code&gt;d54cc35&lt;/code&gt;&lt;/a&gt;
Change example in test cases with no stubs available (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16513&#34;&gt;#16513&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/eb1ee973778e3cf719948e1653db9760ea49405d&#34;&gt;&lt;code&gt;eb1ee97&lt;/code&gt;&lt;/a&gt;
Update hashes in &lt;code&gt;sync-typeshed.py&lt;/code&gt; following recent typeshed
sync (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16600&#34;&gt;#16600&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/344298e3a7b1a299092c684c11c28e9f4dc44dd9&#34;&gt;&lt;code&gt;344298e&lt;/code&gt;&lt;/a&gt;
Revert use of &lt;code&gt;ParamSpec&lt;/code&gt; for
&lt;code&gt;functools.wraps&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3e5d813372e4fc1899319f31425bfc11c27fddb3&#34;&gt;&lt;code&gt;3e5d813&lt;/code&gt;&lt;/a&gt;
Revert typeshed ctypes change&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.7.1...v1.8.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.7.1&amp;new-version=1.8.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`123e423`](https://github.com/Nr18/cfn-guard-test/commit/123e423c737c4e9dbeb74c7dc7ae1fd2f3b028f6))

* chore(deps-dev): Bump python-semantic-release from 8.5.1 to 8.5.2 (#158)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.5.1 to 8.5.2.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.5.2 (2023-12-19)&lt;/h1&gt;
&lt;h2&gt;Build&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): bump ruff from 0.1.7 to 0.1.8 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/775&#34;&gt;#775&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Bumps &lt;a href=&#34;https://github.com/astral-sh/ruff&#34;&gt;ruff&lt;/a&gt; from 0.1.7
to 0.1.8.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href=&#34;https://github.com/astral-sh/ruff/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/compare/v0.1.7...v0.1.8&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: ruff
dependency-type: direct:production
update-type: version-update:semver-patch
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/5efda8acfed938d3188cd55678ace20ecac7f798&#34;&gt;&lt;code&gt;5efda8a&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): bump ruff from 0.1.6 to 0.1.7 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/769&#34;&gt;#769&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): bump ruff from 0.1.6 to 0.1.7&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Bumps &lt;a href=&#34;https://github.com/astral-sh/ruff&#34;&gt;ruff&lt;/a&gt; from 0.1.6
to 0.1.7.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href=&#34;https://github.com/astral-sh/ruff/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/compare/v0.1.6...v0.1.7&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: ruff
dependency-type: direct:production
update-type: version-update:semver-patch
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;ci: remove hardcoded ruff version in workflows&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
Co-authored-by: Bernard Cooke &amp;lt;&lt;a
href=&#34;mailto:bernard-cooke@hotmail.com&#34;&gt;bernard-cooke@hotmail.com&lt;/a&gt;&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/c48c3b370335931d63391d1a4f5802937deff178&#34;&gt;&lt;code&gt;c48c3b3&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;h2&gt;Fix&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;fix(cli): gracefully output configuration validation errors (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/772&#34;&gt;#772&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.5.2 (2023-12-19)&lt;/h2&gt;
&lt;h3&gt;Build&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): bump ruff from 0.1.7 to 0.1.8 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/775&#34;&gt;#775&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Bumps &lt;a href=&#34;https://github.com/astral-sh/ruff&#34;&gt;ruff&lt;/a&gt; from 0.1.7
to 0.1.8.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href=&#34;https://github.com/astral-sh/ruff/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/compare/v0.1.7...v0.1.8&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: ruff
dependency-type: direct:production
update-type: version-update:semver-patch
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/5efda8acfed938d3188cd55678ace20ecac7f798&#34;&gt;&lt;code&gt;5efda8a&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): bump ruff from 0.1.6 to 0.1.7 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/769&#34;&gt;#769&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): bump ruff from 0.1.6 to 0.1.7&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Bumps &lt;a href=&#34;https://github.com/astral-sh/ruff&#34;&gt;ruff&lt;/a&gt; from 0.1.6
to 0.1.7.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href=&#34;https://github.com/astral-sh/ruff/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/compare/v0.1.6...v0.1.7&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: ruff
dependency-type: direct:production
update-type: version-update:semver-patch
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;ci: remove hardcoded ruff version in workflows&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
Co-authored-by: Bernard Cooke &amp;lt;&lt;a
href=&#34;mailto:bernard-cooke@hotmail.com&#34;&gt;bernard-cooke@hotmail.com&lt;/a&gt;&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/c48c3b370335931d63391d1a4f5802937deff178&#34;&gt;&lt;code&gt;c48c3b3&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;h3&gt;Fix&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;fix(cli): gracefully output configuration validation errors (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/772&#34;&gt;#772&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/8476c85a21115ac2dc3a5299d151513a662b53ff&#34;&gt;&lt;code&gt;8476c85&lt;/code&gt;&lt;/a&gt;
8.5.2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/98b10b3f08af16ab5cb00096b288afefbee1b74f&#34;&gt;&lt;code&gt;98b10b3&lt;/code&gt;&lt;/a&gt;
style: beautify 5efda8acfed938d3188cd55678ace20ecac7f798&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/5efda8acfed938d3188cd55678ace20ecac7f798&#34;&gt;&lt;code&gt;5efda8a&lt;/code&gt;&lt;/a&gt;
build(deps-dev): bump ruff from 0.1.7 to 0.1.8 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/775&#34;&gt;#775&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/e8c9d516c37466a5dce75a73766d5be0f9e74627&#34;&gt;&lt;code&gt;e8c9d51&lt;/code&gt;&lt;/a&gt;
fix(cli): gracefully output configuration validation errors (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/772&#34;&gt;#772&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/bb3b63111d0e02bd53c2ed25d5ab0e5a3d532136&#34;&gt;&lt;code&gt;bb3b631&lt;/code&gt;&lt;/a&gt;
style: beautify c48c3b370335931d63391d1a4f5802937deff178&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/c48c3b370335931d63391d1a4f5802937deff178&#34;&gt;&lt;code&gt;c48c3b3&lt;/code&gt;&lt;/a&gt;
build(deps-dev): bump ruff from 0.1.6 to 0.1.7 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/769&#34;&gt;#769&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.5.1...v8.5.2&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.5.1&amp;new-version=8.5.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`1659699`](https://github.com/Nr18/cfn-guard-test/commit/16596992e93d6cd12952e214d660041625679d89))

* chore(deps-dev): Bump python-semantic-release from 8.5.0 to 8.5.1 (#157)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.5.0 to 8.5.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.5.1 (2023-12-12)&lt;/h1&gt;
&lt;h2&gt;Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;docs(configuration): adjust wording and improve clarity (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/766&#34;&gt;#766&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs(configuration): fix typo in text&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs(configuration): adjust wording and improve clarity (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/6b2fc8c156e122ee1b43fdb513b2dc3b8fd76724&#34;&gt;&lt;code&gt;6b2fc8c&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Fix&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;fix(config): gracefully fail when repo is in a detached HEAD state
(&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/765&#34;&gt;#765&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(config): cleanly handle repository in detached HEAD state&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;test(cli-main): add detached head cli test (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/ac4f9aacb72c99f2479ae33369822faad011a824&#34;&gt;&lt;code&gt;ac4f9aa&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(cmd-version): handle committing of git-ignored file gracefully
(&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/764&#34;&gt;#764&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(version): only commit non git-ignored files during version
commit&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;test(version): set version file as ignored file&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Tweaks tests to use one committed change file and the version file
as an ignored change file. This allows us to verify that our commit
mechanism does not crash if a file that is changed is ignored by user
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/ea89fa72885e15da91687172355426a22c152513&#34;&gt;&lt;code&gt;ea89fa7&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;h2&gt;Style&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;style: beautify 6b2fc8c156e122ee1b43fdb513b2dc3b8fd76724 (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9bf69d7005eee75f20b356bda97fea2d250a91de&#34;&gt;&lt;code&gt;9bf69d7&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.5.1 (2023-12-12)&lt;/h2&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;docs(configuration): adjust wording and improve clarity (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/766&#34;&gt;#766&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs(configuration): fix typo in text&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs(configuration): adjust wording and improve clarity (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/6b2fc8c156e122ee1b43fdb513b2dc3b8fd76724&#34;&gt;&lt;code&gt;6b2fc8c&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Fix&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;fix(config): gracefully fail when repo is in a detached HEAD state
(&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/765&#34;&gt;#765&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(config): cleanly handle repository in detached HEAD state&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;test(cli-main): add detached head cli test (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/ac4f9aacb72c99f2479ae33369822faad011a824&#34;&gt;&lt;code&gt;ac4f9aa&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(cmd-version): handle committing of git-ignored file gracefully
(&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/764&#34;&gt;#764&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(version): only commit non git-ignored files during version
commit&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;test(version): set version file as ignored file&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Tweaks tests to use one committed change file and the version file
as an ignored change file. This allows us to verify that our commit
mechanism does not crash if a file that is changed is ignored by user
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/ea89fa72885e15da91687172355426a22c152513&#34;&gt;&lt;code&gt;ea89fa7&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;h3&gt;Style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;style: beautify 6b2fc8c156e122ee1b43fdb513b2dc3b8fd76724 (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9bf69d7005eee75f20b356bda97fea2d250a91de&#34;&gt;&lt;code&gt;9bf69d7&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/0400d7b4f30a5fc1638fd704679871012afb144e&#34;&gt;&lt;code&gt;0400d7b&lt;/code&gt;&lt;/a&gt;
8.5.1&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9bf69d7005eee75f20b356bda97fea2d250a91de&#34;&gt;&lt;code&gt;9bf69d7&lt;/code&gt;&lt;/a&gt;
style: beautify 6b2fc8c156e122ee1b43fdb513b2dc3b8fd76724&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/6b2fc8c156e122ee1b43fdb513b2dc3b8fd76724&#34;&gt;&lt;code&gt;6b2fc8c&lt;/code&gt;&lt;/a&gt;
docs(configuration): adjust wording and improve clarity (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/766&#34;&gt;#766&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/ac4f9aacb72c99f2479ae33369822faad011a824&#34;&gt;&lt;code&gt;ac4f9aa&lt;/code&gt;&lt;/a&gt;
fix(config): gracefully fail when repo is in a detached HEAD state (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/765&#34;&gt;#765&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/ea89fa72885e15da91687172355426a22c152513&#34;&gt;&lt;code&gt;ea89fa7&lt;/code&gt;&lt;/a&gt;
fix(cmd-version): handle committing of git-ignored file gracefully (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/764&#34;&gt;#764&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.5.0...v8.5.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.5.0&amp;new-version=8.5.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`8fbdb8c`](https://github.com/Nr18/cfn-guard-test/commit/8fbdb8c00085fb2d781969f65d9447ddd70306be))

* chore(deps-dev): Bump black from 23.11.0 to 23.12.0 (#156)

Bumps [black](https://github.com/psf/black) from 23.11.0 to 23.12.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;It&#39;s almost 2024, which means it&#39;s time for a new edition of
&lt;em&gt;Black&lt;/em&gt;&#39;s stable style!
Together with this release, we&#39;ll put out an alpha release 24.1a1
showcasing the draft
2024 stable style, which we&#39;ll finalize in the January release. Please
try it out and
&lt;a href=&#34;https://redirect.github.com/psf/black/issues/4042&#34;&gt;share your
feedback&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;This release (23.12.0) will still produce the 2023 style. Most but
not all of the
changes in &lt;code&gt;--preview&lt;/code&gt; mode will be in the 2024 stable
style.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where &lt;code&gt;# fmt: off&lt;/code&gt; automatically dedents when
used with the &lt;code&gt;--line-ranges&lt;/code&gt;
option, even when it is not within the specified line range. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4084&#34;&gt;#4084&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Prefer more equal signs before a break when splitting chained
assignments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4010&#34;&gt;#4010&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Standalone form feed characters at the module level are no longer
removed (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4021&#34;&gt;#4021&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional cases of immediately nested tuples, lists, and
dictionaries are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4012&#34;&gt;#4012&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty lines at the beginning of all blocks, except immediately
before a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash in preview mode when using a short
&lt;code&gt;--line-length&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4086&#34;&gt;#4086&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep suites consisting of only an ellipsis on their own lines if
they are not
functions or class definitions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4103&#34;&gt;#4103&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;--line-ranges&lt;/code&gt; now skips &lt;em&gt;Black&lt;/em&gt;&#39;s internal
stability check in &lt;code&gt;--safe&lt;/code&gt; mode. This
avoids a crash on rare inputs that have many unformatted same-content
lines. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4034&#34;&gt;#4034&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Upgrade to mypy 1.7.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4049&#34;&gt;#4049&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4069&#34;&gt;#4069&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Faster compiled wheels are now available for CPython 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4070&#34;&gt;#4070&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Enable 3.12 CI (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4035&#34;&gt;#4035&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images in parallel (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4054&#34;&gt;#4054&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images with 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4055&#34;&gt;#4055&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;It&#39;s almost 2024, which means it&#39;s time for a new edition of
&lt;em&gt;Black&lt;/em&gt;&#39;s stable style!
Together with this release, we&#39;ll put out an alpha release 24.1a1
showcasing the draft
2024 stable style, which we&#39;ll finalize in the January release. Please
try it out and
&lt;a href=&#34;https://redirect.github.com/psf/black/issues/4042&#34;&gt;share your
feedback&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;This release (23.12.0) will still produce the 2023 style. Most but
not all of the
changes in &lt;code&gt;--preview&lt;/code&gt; mode will be in the 2024 stable
style.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where &lt;code&gt;# fmt: off&lt;/code&gt; automatically dedents when
used with the &lt;code&gt;--line-ranges&lt;/code&gt;
option, even when it is not within the specified line range. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4084&#34;&gt;#4084&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Prefer more equal signs before a break when splitting chained
assignments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4010&#34;&gt;#4010&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Standalone form feed characters at the module level are no longer
removed (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4021&#34;&gt;#4021&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional cases of immediately nested tuples, lists, and
dictionaries are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4012&#34;&gt;#4012&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty lines at the beginning of all blocks, except immediately
before a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash in preview mode when using a short
&lt;code&gt;--line-length&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4086&#34;&gt;#4086&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep suites consisting of only an ellipsis on their own lines if
they are not
functions or class definitions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4103&#34;&gt;#4103&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;--line-ranges&lt;/code&gt; now skips &lt;em&gt;Black&lt;/em&gt;&#39;s internal
stability check in &lt;code&gt;--safe&lt;/code&gt; mode. This
avoids a crash on rare inputs that have many unformatted same-content
lines. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4034&#34;&gt;#4034&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Upgrade to mypy 1.7.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4049&#34;&gt;#4049&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4069&#34;&gt;#4069&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Faster compiled wheels are now available for CPython 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4070&#34;&gt;#4070&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Enable 3.12 CI (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4035&#34;&gt;#4035&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images in parallel (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4054&#34;&gt;#4054&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images with 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4055&#34;&gt;#4055&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/d9ad09a32b0e0481bb4fef548d35b7a49cc03c5d&#34;&gt;&lt;code&gt;d9ad09a&lt;/code&gt;&lt;/a&gt;
Prepare release 23.12.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4105&#34;&gt;#4105&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ebd543c0ac9b8a5f17636d0a42c425e5f693860e&#34;&gt;&lt;code&gt;ebd543c&lt;/code&gt;&lt;/a&gt;
Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/eb7661f8ab9bff344835693c7c08789bb195137e&#34;&gt;&lt;code&gt;eb7661f&lt;/code&gt;&lt;/a&gt;
Fix another case where we format dummy implementation for
non-functions/class...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/0c9899956d890a9dc9c3adbc80b478a47846ced9&#34;&gt;&lt;code&gt;0c98999&lt;/code&gt;&lt;/a&gt;
Fix path in test message (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4102&#34;&gt;#4102&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/9aea9768cb60d23f2f4d331e94c4ee07ef1683a5&#34;&gt;&lt;code&gt;9aea976&lt;/code&gt;&lt;/a&gt;
Only use dummy implementation logic for functions and classes (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/67b23d71854c19921cc6092c695d3301ab99229c&#34;&gt;&lt;code&gt;67b23d7&lt;/code&gt;&lt;/a&gt;
Bump actions/setup-python from 4 to 5 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4101&#34;&gt;#4101&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ce28be2705ab29f184ec4a00aa3d23340630796d&#34;&gt;&lt;code&gt;ce28be2&lt;/code&gt;&lt;/a&gt;
Add dedicated preview feature for East Asian Width (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4097&#34;&gt;#4097&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/61b529b7d15400309379f36104885a1dfcd2d026&#34;&gt;&lt;code&gt;61b529b&lt;/code&gt;&lt;/a&gt;
Allow empty lines at beginning of blocks (again) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e7e122e9ff27fc040a6e8ecd92f0e7603c87f92d&#34;&gt;&lt;code&gt;e7e122e&lt;/code&gt;&lt;/a&gt;
docs: Move &lt;code&gt;fmt: off&lt;/code&gt; docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4090&#34;&gt;#4090&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/432d9050c3d1e35a36ffc97d4a9e0e0c9e5e4ecc&#34;&gt;&lt;code&gt;432d905&lt;/code&gt;&lt;/a&gt;
docs: Unify option descriptions between &lt;code&gt;--help&lt;/code&gt; and
&lt;code&gt;the_basics.md&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4076&#34;&gt;#4076&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.11.0...23.12.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.11.0&amp;new-version=23.12.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`303b865`](https://github.com/Nr18/cfn-guard-test/commit/303b8659741fcc9137e8d16781292b5248d9bd1e))

* chore(deps-dev): Bump python-semantic-release from 8.4.0 to 8.5.0 (#155)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.4.0 to 8.5.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.5.0 (2023-12-07)&lt;/h1&gt;
&lt;h2&gt;Feature&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;feat: allow template directories to contain a &amp;amp;&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/39&#34;&gt;#39&lt;/a&gt;;.&amp;amp;&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/39&#34;&gt;#39&lt;/a&gt;;
at the top-level (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/762&#34;&gt;#762&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/07b232a3b34be0b28c6af08aea4852acb1b9bd56&#34;&gt;&lt;code&gt;07b232a&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.5.0 (2023-12-07)&lt;/h2&gt;
&lt;h3&gt;Feature&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;feat: allow template directories to contain a &amp;amp;&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/39&#34;&gt;#39&lt;/a&gt;;.&amp;amp;&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/39&#34;&gt;#39&lt;/a&gt;;
at the top-level (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/762&#34;&gt;#762&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/07b232a3b34be0b28c6af08aea4852acb1b9bd56&#34;&gt;&lt;code&gt;07b232a&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/3a571d2622de93fab7844465db9c442846c8b78d&#34;&gt;&lt;code&gt;3a571d2&lt;/code&gt;&lt;/a&gt;
8.5.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/07b232a3b34be0b28c6af08aea4852acb1b9bd56&#34;&gt;&lt;code&gt;07b232a&lt;/code&gt;&lt;/a&gt;
feat: allow template directories to contain a &#39;.&#39; at the top-level (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/762&#34;&gt;#762&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.4.0...v8.5.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.4.0&amp;new-version=8.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`2ded97e`](https://github.com/Nr18/cfn-guard-test/commit/2ded97e6bd29cf4142acc3951b7b9547677271dd))

* chore(deps-dev): Bump python-semantic-release from 8.3.0 to 8.4.0 (#154)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.3.0 to 8.4.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.4.0 (2023-12-07)&lt;/h1&gt;
&lt;h2&gt;Build&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): bump ruff from 0.1.2 to 0.1.6 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/757&#34;&gt;#757&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Bumps &lt;a href=&#34;https://github.com/astral-sh/ruff&#34;&gt;ruff&lt;/a&gt; from 0.1.2
to 0.1.6.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href=&#34;https://github.com/astral-sh/ruff/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/compare/v0.1.2...v0.1.6&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: ruff
dependency-type: direct:production
update-type: version-update:semver-patch
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/90db8f1bd8986eda1b913cd4bab5abd41192f01f&#34;&gt;&lt;code&gt;90db8f1&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): update python-gitlab requirement from &amp;lt;4,&amp;gt;=2
to &amp;gt;=2,&amp;lt;5 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/748&#34;&gt;#748&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Updates the requirements on &lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab&#34;&gt;python-gitlab&lt;/a&gt;
to permit the latest version.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab/compare/v2.0.0...v4.1.1&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: python-gitlab
dependency-type: direct:production
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/a176d626f28ba68ae8a938b2f04f74da841a7eeb&#34;&gt;&lt;code&gt;a176d62&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): bump ruff from 0.0.292 to 0.1.1 (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9c5bbe0b0ef96e0fadae9e65918fc8939d0d3e60&#34;&gt;&lt;code&gt;9c5bbe0&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;docs(migration): fix comments about publish command (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/747&#34;&gt;#747&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/90380d797a734dcca5040afc5fa00e3e01f64152&#34;&gt;&lt;code&gt;90380d7&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Feature&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;feat(cmd-version): add &lt;code&gt;--tag/--no-tag&lt;/code&gt; option to version
command (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/752&#34;&gt;#752&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(version): separate push tags from commit push when not committing
changes&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;feat(version): add &lt;code&gt;--no-tag&lt;/code&gt; option to turn off tag
creation&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.4.0 (2023-12-07)&lt;/h2&gt;
&lt;h3&gt;Build&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): bump ruff from 0.1.2 to 0.1.6 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/757&#34;&gt;#757&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Bumps &lt;a href=&#34;https://github.com/astral-sh/ruff&#34;&gt;ruff&lt;/a&gt; from 0.1.2
to 0.1.6.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a href=&#34;https://github.com/astral-sh/ruff/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/astral-sh/ruff/compare/v0.1.2...v0.1.6&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: ruff
dependency-type: direct:production
update-type: version-update:semver-patch
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/90db8f1bd8986eda1b913cd4bab5abd41192f01f&#34;&gt;&lt;code&gt;90db8f1&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): update python-gitlab requirement from &amp;lt;4,&amp;gt;=2
to &amp;gt;=2,&amp;lt;5 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/748&#34;&gt;#748&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Updates the requirements on &lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab&#34;&gt;python-gitlab&lt;/a&gt;
to permit the latest version.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab/releases&#34;&gt;Release
notes&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab/blob/main/CHANGELOG.md&#34;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-gitlab/python-gitlab/compare/v2.0.0...v4.1.1&#34;&gt;Commits&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;hr /&gt;
&lt;p&gt;updated-dependencies:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;dependency-name: python-gitlab
dependency-type: direct:production
...&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: dependabot[bot] &amp;lt;&lt;a
href=&#34;mailto:support@github.com&#34;&gt;support@github.com&lt;/a&gt;&amp;gt;
Co-authored-by: dependabot[bot] &amp;lt;49699333+dependabot[bot]&lt;a
href=&#34;https://github.com/users&#34;&gt;&lt;code&gt;@​users&lt;/code&gt;&lt;/a&gt;.noreply.github.com&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/a176d626f28ba68ae8a938b2f04f74da841a7eeb&#34;&gt;&lt;code&gt;a176d62&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;build(deps-dev): bump ruff from 0.0.292 to 0.1.1 (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9c5bbe0b0ef96e0fadae9e65918fc8939d0d3e60&#34;&gt;&lt;code&gt;9c5bbe0&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;docs(migration): fix comments about publish command (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/747&#34;&gt;#747&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/90380d797a734dcca5040afc5fa00e3e01f64152&#34;&gt;&lt;code&gt;90380d7&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Feature&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;feat(cmd-version): add &lt;code&gt;--tag/--no-tag&lt;/code&gt; option to version
command (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/752&#34;&gt;#752&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix(version): separate push tags from commit push when not committing
changes&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;feat(version): add &lt;code&gt;--no-tag&lt;/code&gt; option to turn off tag
creation&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/aa9b33b9e4001f9d9071797e16f144a9f6b90fb5&#34;&gt;&lt;code&gt;aa9b33b&lt;/code&gt;&lt;/a&gt;
8.4.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/c94fb6f53bd8bdeaa4f40219886fa7c6e8755f29&#34;&gt;&lt;code&gt;c94fb6f&lt;/code&gt;&lt;/a&gt;
style: beautify de6b9ad921e697b5ea2bb2ea8f180893cecca920&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/de6b9ad921e697b5ea2bb2ea8f180893cecca920&#34;&gt;&lt;code&gt;de6b9ad&lt;/code&gt;&lt;/a&gt;
feat(cmd-version): add &lt;code&gt;--tag/--no-tag&lt;/code&gt; option to version
command (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/752&#34;&gt;#752&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/744ff256f10c895a97241dc085bc132d10c9f737&#34;&gt;&lt;code&gt;744ff25&lt;/code&gt;&lt;/a&gt;
test(commandline-main): prevent git gpgsign config from failing tests
(&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/760&#34;&gt;#760&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/90380d797a734dcca5040afc5fa00e3e01f64152&#34;&gt;&lt;code&gt;90380d7&lt;/code&gt;&lt;/a&gt;
docs(migration): fix comments about publish command (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/747&#34;&gt;#747&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/90db8f1bd8986eda1b913cd4bab5abd41192f01f&#34;&gt;&lt;code&gt;90db8f1&lt;/code&gt;&lt;/a&gt;
build(deps-dev): bump ruff from 0.1.2 to 0.1.6 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/757&#34;&gt;#757&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/a176d626f28ba68ae8a938b2f04f74da841a7eeb&#34;&gt;&lt;code&gt;a176d62&lt;/code&gt;&lt;/a&gt;
build(deps-dev): update python-gitlab requirement from &amp;lt;4,&amp;gt;=2 to
&amp;gt;=2,&amp;lt;5 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/748&#34;&gt;#748&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/deb4dbaba3de5396e0eb2389e728d0b1fe702843&#34;&gt;&lt;code&gt;deb4dba&lt;/code&gt;&lt;/a&gt;
style: convert formatter from black to ruff (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/746&#34;&gt;#746&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/f1452578cc064edbe64d61ae3baab4bc9bd4b666&#34;&gt;&lt;code&gt;f145257&lt;/code&gt;&lt;/a&gt;
Revert &amp;quot;feat(action): use composite action for semantic release (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/692&#34;&gt;#692&lt;/a&gt;)&amp;quot;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9c5bbe0b0ef96e0fadae9e65918fc8939d0d3e60&#34;&gt;&lt;code&gt;9c5bbe0&lt;/code&gt;&lt;/a&gt;
build(deps-dev): bump ruff from 0.0.292 to 0.1.1&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.3.0...v8.4.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.3.0&amp;new-version=8.4.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`90795b9`](https://github.com/Nr18/cfn-guard-test/commit/90795b9679f75d592dcd870344bfd44472fa30c7))

* chore(deps-dev): Bump mypy from 1.7.0 to 1.7.1 (#153)

Bumps [mypy](https://github.com/python/mypy) from 1.7.0 to 1.7.1.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6b3c41838d8e7a39242b6fd035535e2d76eabfc6&#34;&gt;&lt;code&gt;6b3c418&lt;/code&gt;&lt;/a&gt;
Update version to 1.7.1 (without +dev)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c10e17348f2eacbbeae80eb6c10c661c0137d849&#34;&gt;&lt;code&gt;c10e173&lt;/code&gt;&lt;/a&gt;
[mypyc] Fix regression with nested functions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16484&#34;&gt;#16484&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/e6399d10b0a1cdb104559482fad1b4dc0e2de6ac&#34;&gt;&lt;code&gt;e6399d1&lt;/code&gt;&lt;/a&gt;
Fix polymorphic application for callback protocols (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16514&#34;&gt;#16514&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/661adb756800ecc40fabbe62e9339efd253aff4e&#34;&gt;&lt;code&gt;661adb7&lt;/code&gt;&lt;/a&gt;
Fix crash on strict-equality with recursive types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16483&#34;&gt;#16483&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6c8e0cc47c014894ea41621a10f3d1b465322362&#34;&gt;&lt;code&gt;6c8e0cc&lt;/code&gt;&lt;/a&gt;
Ignore position if imprecise arguments are matched by name (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16471&#34;&gt;#16471&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/5c354c41c0fbb74418afcbd30ba822694be28d11&#34;&gt;&lt;code&gt;5c354c4&lt;/code&gt;&lt;/a&gt;
Fix missing meet case exposed by len narrowing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16470&#34;&gt;#16470&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/88791cabe0521f77b699405154d90f3bb7c6b31b&#34;&gt;&lt;code&gt;88791ca&lt;/code&gt;&lt;/a&gt;
Exclude private attributes from override checks (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16464&#34;&gt;#16464&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/4b5b316beb570bba4c9b7797deb2e6d7df0552d0&#34;&gt;&lt;code&gt;4b5b316&lt;/code&gt;&lt;/a&gt;
Special-case unions in polymorphic inference (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16461&#34;&gt;#16461&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f862d3ef540c38e7efd2fffd64fc732d6318dfb4&#34;&gt;&lt;code&gt;f862d3e&lt;/code&gt;&lt;/a&gt;
Fix crash on Callable self in &lt;strong&gt;call&lt;/strong&gt; (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16453&#34;&gt;#16453&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/fe79a59e44299a3cc8025aa5084e08773c872a54&#34;&gt;&lt;code&gt;fe79a59&lt;/code&gt;&lt;/a&gt;
Bump version to 1.7.1+dev&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.7.0...v1.7.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.7.0&amp;new-version=1.7.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`d8e4228`](https://github.com/Nr18/cfn-guard-test/commit/d8e422843650e191a368215f1d2d816152355aca))

* chore(deps-dev): Bump mypy from 1.6.1 to 1.7.0 (#152)

Bumps [mypy](https://github.com/python/mypy) from 1.6.1 to 1.7.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python/mypy/blob/master/CHANGELOG.md&#34;&gt;mypy&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;Mypy Release Notes&lt;/h1&gt;
&lt;h2&gt;Next release&lt;/h2&gt;
&lt;p&gt;Stubgen will now include &lt;code&gt;__all__&lt;/code&gt; in its output if it is
in the input file (PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16356&#34;&gt;16356&lt;/a&gt;).&lt;/p&gt;
&lt;h2&gt;Mypy 1.7&lt;/h2&gt;
&lt;p&gt;We’ve just uploaded mypy 1.7 to the Python Package Index (&lt;a
href=&#34;https://pypi.org/project/mypy/&#34;&gt;PyPI&lt;/a&gt;). Mypy is a static type
checker for Python. This release includes new features, performance
improvements and bug fixes. You can install it as follows:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;python3 -m pip install -U mypy
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;You can read the full documentation for this release on &lt;a
href=&#34;http://mypy.readthedocs.io&#34;&gt;Read the Docs&lt;/a&gt;.&lt;/p&gt;
&lt;h4&gt;Using TypedDict for &lt;code&gt;**kwargs&lt;/code&gt; Typing&lt;/h4&gt;
&lt;p&gt;Mypy now has support for using &lt;code&gt;Unpack[...]&lt;/code&gt; with a
TypedDict type to annotate &lt;code&gt;**kwargs&lt;/code&gt; arguments enabled by
default. Example:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;# Or &#39;from typing_extensions import ...&#39;
from typing import TypedDict, Unpack
&lt;p&gt;class Person(TypedDict):
name: str
age: int&lt;/p&gt;
&lt;p&gt;def foo(**kwargs: Unpack[Person]) -&amp;gt; None:
...&lt;/p&gt;
&lt;p&gt;foo(name=&amp;quot;x&amp;quot;, age=1)  # Ok
foo(name=1)  # Error
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;p&gt;The definition of &lt;code&gt;foo&lt;/code&gt; above is equivalent to the one
below, with keyword-only arguments &lt;code&gt;name&lt;/code&gt; and
&lt;code&gt;age&lt;/code&gt;:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;def foo(*, name: str, age: int) -&amp;gt; None:
    ...
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;Refer to &lt;a href=&#34;https://peps.python.org/pep-0692/&#34;&gt;PEP 692&lt;/a&gt; for
more information. Note that unlike in the current version of the PEP,
mypy always treats signatures with &lt;code&gt;Unpack[SomeTypedDict]&lt;/code&gt; as
equivalent to their expanded forms with explicit keyword arguments, and
there aren&#39;t special type checking rules for TypedDict arguments.&lt;/p&gt;
&lt;p&gt;This was contributed by Ivan Levkivskyi back in 2022 (PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/13471&#34;&gt;13471&lt;/a&gt;).&lt;/p&gt;
&lt;h4&gt;TypeVarTuple Support Enabled (Experimental)&lt;/h4&gt;
&lt;p&gt;Mypy now has support for variadic generics (TypeVarTuple) enabled by
default, as an experimental feature. Refer to &lt;a
href=&#34;https://peps.python.org/pep-0646/&#34;&gt;PEP 646&lt;/a&gt; for the
details.&lt;/p&gt;
&lt;p&gt;TypeVarTuple was implemented by Jared Hance and Ivan Levkivskyi over
several mypy releases, with help from Jukka Lehtosalo.&lt;/p&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f6b9972329d5d68f6defc92a10cc4c3bc339c27b&#34;&gt;&lt;code&gt;f6b9972&lt;/code&gt;&lt;/a&gt;
Remove +dev from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/62bcae2d9bad12c5d3b5dda23dc031e1c7ddf136&#34;&gt;&lt;code&gt;62bcae2&lt;/code&gt;&lt;/a&gt;
Fix handling of tuple type context with unpacks (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16444&#34;&gt;#16444&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c22294a80b000ea673e407994ac5111644944486&#34;&gt;&lt;code&gt;c22294a&lt;/code&gt;&lt;/a&gt;
Handle TypeVarTupleType when checking overload constraints (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16428&#34;&gt;#16428&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/8813968abb657113df5edfa207db46b0649c9dce&#34;&gt;&lt;code&gt;8813968&lt;/code&gt;&lt;/a&gt;
Fix type narrowing in lambda expressions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16407&#34;&gt;#16407&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/681e54cfe1642adddc41c4ff11198b8bc955d5af&#34;&gt;&lt;code&gt;681e54c&lt;/code&gt;&lt;/a&gt;
Fix crash on unpack call special-casing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16381&#34;&gt;#16381&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f68f46351e30644aefd19900ba1634595adc1d09&#34;&gt;&lt;code&gt;f68f463&lt;/code&gt;&lt;/a&gt;
Fix file reloading in dmypy with --export-types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16359&#34;&gt;#16359&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/5624f401b3786ebdbe167c27297ed778cce3faa5&#34;&gt;&lt;code&gt;5624f40&lt;/code&gt;&lt;/a&gt;
Fix daemon crash caused by deleted submodule (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16370&#34;&gt;#16370&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/ad0e183b0df7cc3dd94d9e1cd6f5710859beda96&#34;&gt;&lt;code&gt;ad0e183&lt;/code&gt;&lt;/a&gt;
Enable Unpack/TypeVarTuple support (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16354&#34;&gt;#16354&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/b064a5c183b53a84d895bb8e3c36a3a74e24be9c&#34;&gt;&lt;code&gt;b064a5c&lt;/code&gt;&lt;/a&gt;
Fix dmypy inspect on Windows (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16355&#34;&gt;#16355&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/4e30e896486b774cdecaef6d3521a585b8acf8bc&#34;&gt;&lt;code&gt;4e30e89&lt;/code&gt;&lt;/a&gt;
Fix dmypy inspect for namespace packages (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16357&#34;&gt;#16357&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.6.1...v1.7.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.6.1&amp;new-version=1.7.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`a391902`](https://github.com/Nr18/cfn-guard-test/commit/a391902eecc5a26e1b04b65a6dbb0b1574ecf8a8))

* chore(deps-dev): Bump black from 23.10.1 to 23.11.0 (#151)

Bumps [black](https://github.com/psf/black) from 23.10.1 to 23.11.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.11.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Support formatting ranges of lines with the new
&lt;code&gt;--line-ranges&lt;/code&gt; command-line option
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash on formatting bytes strings that look like docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4003&#34;&gt;#4003&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash when whitespace followed a backslash before newline in a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4008&#34;&gt;#4008&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on formatting code like &lt;code&gt;await (a ** b)&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3994&#34;&gt;#3994&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;No longer treat leading f-strings as docstrings. This matches
Python&#39;s behaviour and
fixes a crash (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Multiline dicts and lists that are the sole argument to a function
are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3964&#34;&gt;#3964&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Multiline unpacked dicts and lists as the sole argument to a
function are now also
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3992&#34;&gt;#3992&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;In f-string debug expressions, quote types that are visible in the
final string
are now preserved (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug where long &lt;code&gt;case&lt;/code&gt; blocks were not split into
multiple lines. Also enable
general trailing comma rules on &lt;code&gt;case&lt;/code&gt; blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep requiring two empty lines between module-level docstring and
first function or
class definition (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for single-line format skip with other comments on the
same line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently apply force exclusion logic before resolving symlinks
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug in the matching of absolute path names in
&lt;code&gt;--include&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3976&#34;&gt;#3976&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Performance&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix mypyc builds on arm64 on macOS (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4017&#34;&gt;#4017&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black&#39;s pre-commit integration will now run only on git hooks
appropriate for a code
formatter (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3940&#34;&gt;#3940&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.11.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Support formatting ranges of lines with the new
&lt;code&gt;--line-ranges&lt;/code&gt; command-line option
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash on formatting bytes strings that look like docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4003&#34;&gt;#4003&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash when whitespace followed a backslash before newline in a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4008&#34;&gt;#4008&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on formatting code like &lt;code&gt;await (a ** b)&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3994&#34;&gt;#3994&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;No longer treat leading f-strings as docstrings. This matches
Python&#39;s behaviour and
fixes a crash (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Multiline dicts and lists that are the sole argument to a function
are now indented
less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3964&#34;&gt;#3964&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Multiline unpacked dicts and lists as the sole argument to a
function are now also
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3992&#34;&gt;#3992&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;In f-string debug expressions, quote types that are visible in the
final string are
now preserved (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug where long &lt;code&gt;case&lt;/code&gt; blocks were not split into
multiple lines. Also enable
general trailing comma rules on &lt;code&gt;case&lt;/code&gt; blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep requiring two empty lines between module-level docstring and
first function or
class definition (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for single-line format skip with other comments on the
same line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently apply force exclusion logic before resolving symlinks
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug in the matching of absolute path names in
&lt;code&gt;--include&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3976&#34;&gt;#3976&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Performance&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix mypyc builds on arm64 on macOS (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4017&#34;&gt;#4017&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black&#39;s pre-commit integration will now run only on git hooks
appropriate for a code
formatter (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3940&#34;&gt;#3940&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2a1c67e0b2f81df602ec1f6e7aeb030b9709dc7c&#34;&gt;&lt;code&gt;2a1c67e&lt;/code&gt;&lt;/a&gt;
Prepare release 23.11.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4032&#34;&gt;#4032&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/72e7a2e43eef2aa0c83652bb6725eb004a2a69f3&#34;&gt;&lt;code&gt;72e7a2e&lt;/code&gt;&lt;/a&gt;
Remove redundant condition from &lt;code&gt;has_magic_trailing_comma&lt;/code&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4023&#34;&gt;#4023&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1a7d9c2f58de1ffcbbe6d133f60f283601ba3f54&#34;&gt;&lt;code&gt;1a7d9c2&lt;/code&gt;&lt;/a&gt;
Preserve visible quote types for f-string debug expressions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/f4c7be5445c87d9af5eba3d12faea62d2635e3d8&#34;&gt;&lt;code&gt;f4c7be5&lt;/code&gt;&lt;/a&gt;
docs: fix minor typo (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4030&#34;&gt;#4030&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2e4fac9d87615e904a49e46a9cab2293e0b13126&#34;&gt;&lt;code&gt;2e4fac9&lt;/code&gt;&lt;/a&gt;
Apply force exclude logic before symlink resolution (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/66008fda5dc07f5626e5f5d0dcefc476a9c12ab8&#34;&gt;&lt;code&gt;66008fd&lt;/code&gt;&lt;/a&gt;
[563] Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/50ed6221d97b265025abaa66116a7b185f2df5e2&#34;&gt;&lt;code&gt;50ed622&lt;/code&gt;&lt;/a&gt;
Fix long case blocks not split into multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/46be1f8e54ac9a7d67723c0fa28c7bec13a0a2bf&#34;&gt;&lt;code&gt;46be1f8&lt;/code&gt;&lt;/a&gt;
Support formatting specified lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ecbd9e8cf71f13068c7e6803a534e00363114c91&#34;&gt;&lt;code&gt;ecbd9e8&lt;/code&gt;&lt;/a&gt;
Fix crash with f-string docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e808e61db8c7a8f9c7fd4b2fff2281141f6b2517&#34;&gt;&lt;code&gt;e808e61&lt;/code&gt;&lt;/a&gt;
Preview: Keep requiring two empty lines between module-level docstring
and fi...&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.10.1...23.11.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.10.1&amp;new-version=23.11.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`e7c9275`](https://github.com/Nr18/cfn-guard-test/commit/e7c927504091daee2da83123d3bd8bcc5dbe688d))

* chore(deps-dev): Bump pytest from 7.4.2 to 7.4.3 (#150)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.2 to
7.4.3.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;pytest 7.4.3 (2023-10-24)&lt;/h2&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/10447&#34;&gt;#10447&lt;/a&gt;:
Markers are now considered in the reverse mro order to ensure base class
markers are considered first -- this resolves a regression.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11239&#34;&gt;#11239&lt;/a&gt;:
Fixed &lt;code&gt;:=&lt;/code&gt; in asserts impacting unrelated test cases.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11439&#34;&gt;#11439&lt;/a&gt;:
Handled an edge case where :data:&lt;code&gt;sys.stderr&lt;/code&gt; might already
be closed when :ref:&lt;code&gt;faulthandler&lt;/code&gt; is tearing down.&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/23906106968eb95afbd61adfbc7bbb795fc9aaa9&#34;&gt;&lt;code&gt;2390610&lt;/code&gt;&lt;/a&gt;
Tweak changelog.rst&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a0714aa0076f38e6fb8c7321e8bb4f5f33d1792d&#34;&gt;&lt;code&gt;a0714aa&lt;/code&gt;&lt;/a&gt;
Prepare release version 7.4.3&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/44ad1c9811d2ebf540e601ea66b9bebf8ea82969&#34;&gt;&lt;code&gt;44ad1c9&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/10447&#34;&gt;#10447&lt;/a&gt;
- consider marks in reverse mro order to give base classes...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/5dc77253d439038ac64c55a5a48692ac3a53db2e&#34;&gt;&lt;code&gt;5dc7725&lt;/code&gt;&lt;/a&gt;
[7.4.x] Ensure logging tests always cleanup after themselves (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11541&#34;&gt;#11541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a5178273183ddbda0ef4e4c6aa2b92aab086776b&#34;&gt;&lt;code&gt;a517827&lt;/code&gt;&lt;/a&gt;
[7.4.x] Configure ReadTheDocs to fail on warnings (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11540&#34;&gt;#11540&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/21fe071d797612468fa18dd0ae4d6dbf49846b6d&#34;&gt;&lt;code&gt;21fe071&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix for ValueError raised in faulthandler teardown code (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11455&#34;&gt;#11455&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/f8bb8572fed8627946bfc82819d24b138d587257&#34;&gt;&lt;code&gt;f8bb857&lt;/code&gt;&lt;/a&gt;
Force terminal width when running tests (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11425&#34;&gt;#11425&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11432&#34;&gt;#11432&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/1944dc06d39404ae9869b544dc2e2b482bf472e2&#34;&gt;&lt;code&gt;1944dc0&lt;/code&gt;&lt;/a&gt;
[7.4.x] Fix --import-mode=importlib when root contains
&lt;code&gt;__init__.py&lt;/code&gt; file (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/1&#34;&gt;#1&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/946634c84cf074a1ead10bdba56ddf3e5408e95c&#34;&gt;&lt;code&gt;946634c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11419&#34;&gt;#11419&lt;/a&gt;
from nicoddemus/backport-11414-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d849a3ed64c6da63a0e3713892a7bfefdd56acaf&#34;&gt;&lt;code&gt;d849a3e&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix: closes &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11343&#34;&gt;#11343&lt;/a&gt;&#39;s
[attr-defined] type errors (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11421&#34;&gt;#11421&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/7.4.2...7.4.3&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=7.4.2&amp;new-version=7.4.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`b9047b8`](https://github.com/Nr18/cfn-guard-test/commit/b9047b80aedc7c3818ddb5c031ff55cbd3c95334))

* chore(deps-dev): Bump black from 23.10.0 to 23.10.1 (#149)

Bumps [black](https://github.com/psf/black) from 23.10.0 to 23.10.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.1&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Maintanence release to get a fix out for GitHub Action edge case (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first line after block open before a comment or compound
statement (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Change Dockerfile to hatch + compile black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The summary output for GitHub workflows is now suppressible using
the &lt;code&gt;summary&lt;/code&gt;
parameter. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix the action failing when Black check doesn&#39;t pass (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;It is known Windows documentation CI is broken
&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3968&#34;&gt;psf/black#3968&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.1&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Maintanence release to get a fix out for GitHub Action edge case (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first line after block open before a comment or compound
statement (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Change Dockerfile to hatch + compile black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The summary output for GitHub workflows is now suppressible using
the &lt;code&gt;summary&lt;/code&gt;
parameter. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix the action failing when Black check doesn&#39;t pass (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;It is known Windows documentation CI is broken
&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3968&#34;&gt;psf/black#3968&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/744d23b34800c06e10272149b70752396e90eeb8&#34;&gt;&lt;code&gt;744d23b&lt;/code&gt;&lt;/a&gt;
Prepare release 23.10.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3969&#34;&gt;#3969&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8de4be516879302afce542ac80a6a43ced807759&#34;&gt;&lt;code&gt;8de4be5&lt;/code&gt;&lt;/a&gt;
Fix CI failing (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/c0adca321dc0d97a704de8ed0353e5b894a6a912&#34;&gt;&lt;code&gt;c0adca3&lt;/code&gt;&lt;/a&gt;
docs: specifies the use of the .git-blame-ignore-revs file (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3961&#34;&gt;#3961&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/a7643fac8d97c15640a2b1a79f68b3dc771aebfb&#34;&gt;&lt;code&gt;a7643fa&lt;/code&gt;&lt;/a&gt;
Add summary parameter to action (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/d291c2338c3c1feee4f3f26985c0964ec1b7eb9f&#34;&gt;&lt;code&gt;d291c23&lt;/code&gt;&lt;/a&gt;
Move Docker image to hatch + compile (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7f1c578b89b2c256a6ce3b70fc1b970b3ffa3349&#34;&gt;&lt;code&gt;7f1c578&lt;/code&gt;&lt;/a&gt;
Bump peter-evans/create-or-update-comment from 3.0.2 to 3.1.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3966&#34;&gt;#3966&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2db5ab0a7b3b321e4cec70964239ee88087cd810&#34;&gt;&lt;code&gt;2db5ab0&lt;/code&gt;&lt;/a&gt;
Allow empty line after block open before a comment or compound statement
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/0a37888e79059018eef9293a724b14da59d3377a&#34;&gt;&lt;code&gt;0a37888&lt;/code&gt;&lt;/a&gt;
Fix typos in CHANGES.md (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3963&#34;&gt;#3963&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/882d8795c6ff65c02f2657e596391748d1b6b7f5&#34;&gt;&lt;code&gt;882d879&lt;/code&gt;&lt;/a&gt;
Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/psf/black/compare/23.10.0...23.10.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.10.0&amp;new-version=23.10.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`9da3607`](https://github.com/Nr18/cfn-guard-test/commit/9da36075c88cb95b1b10445f8cde38527ca0c4e5))

* chore(deps-dev): Bump python-semantic-release from 8.2.0 to 8.3.0 (#148)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.2.0 to 8.3.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.3.0 (2023-10-23)&lt;/h1&gt;
&lt;h2&gt;Feature&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;feat(action): use composite action for semantic release (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/692&#34;&gt;#692&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Co-authored-by: Bernard Cooke &amp;lt;&lt;a
href=&#34;mailto:bernard-cooke@hotmail.com&#34;&gt;bernard-cooke@hotmail.com&lt;/a&gt;&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/4648d87bac8fb7e6cc361b765b4391b30a8caef8&#34;&gt;&lt;code&gt;4648d87&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.3.0 (2023-10-23)&lt;/h2&gt;
&lt;h3&gt;Feature&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;feat(action): use composite action for semantic release (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/692&#34;&gt;#692&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Co-authored-by: Bernard Cooke &amp;lt;&lt;a
href=&#34;mailto:bernard-cooke@hotmail.com&#34;&gt;bernard-cooke@hotmail.com&lt;/a&gt;&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/4648d87bac8fb7e6cc361b765b4391b30a8caef8&#34;&gt;&lt;code&gt;4648d87&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/d38d71ef2ae2b3c34066557ddb822385c1730c7f&#34;&gt;&lt;code&gt;d38d71e&lt;/code&gt;&lt;/a&gt;
8.3.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/4648d87bac8fb7e6cc361b765b4391b30a8caef8&#34;&gt;&lt;code&gt;4648d87&lt;/code&gt;&lt;/a&gt;
feat(action): use composite action for semantic release (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/692&#34;&gt;#692&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.2.0...v8.3.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.2.0&amp;new-version=8.3.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`5a8c376`](https://github.com/Nr18/cfn-guard-test/commit/5a8c3769767ae4c6e0199f709bbdfa98a70b0ab2))

* chore(deps-dev): bump python-semantic-release from 8.1.2 to 8.2.0 (#147)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.1.2 to 8.2.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.2.0 (2023-10-23)&lt;/h1&gt;
&lt;h2&gt;Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;docs: add PYTHONPATH mention for commit parser (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/3284258b9fa1a3fe165f336181aff831d50fddd3&#34;&gt;&lt;code&gt;3284258&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Feature&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;feat: Allow user customization of release notes template (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/736&#34;&gt;#736&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: Bryant Finney &amp;lt;&lt;a
href=&#34;mailto:bryant.finney@outlook.com&#34;&gt;bryant.finney@outlook.com&lt;/a&gt;&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/94a131167e1b867f8bc112a042b9766e050ccfd1&#34;&gt;&lt;code&gt;94a1311&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.2.0 (2023-10-23)&lt;/h2&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;docs: add PYTHONPATH mention for commit parser (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/3284258b9fa1a3fe165f336181aff831d50fddd3&#34;&gt;&lt;code&gt;3284258&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Feature&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;feat: Allow user customization of release notes template (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/736&#34;&gt;#736&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Signed-off-by: Bryant Finney &amp;lt;&lt;a
href=&#34;mailto:bryant.finney@outlook.com&#34;&gt;bryant.finney@outlook.com&lt;/a&gt;&amp;gt;
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/94a131167e1b867f8bc112a042b9766e050ccfd1&#34;&gt;&lt;code&gt;94a1311&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/0bef416fa948479c6a1c0508ef66cf311ce6a7ad&#34;&gt;&lt;code&gt;0bef416&lt;/code&gt;&lt;/a&gt;
8.2.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/94a131167e1b867f8bc112a042b9766e050ccfd1&#34;&gt;&lt;code&gt;94a1311&lt;/code&gt;&lt;/a&gt;
feat: Allow user customization of release notes template (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/736&#34;&gt;#736&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/3284258b9fa1a3fe165f336181aff831d50fddd3&#34;&gt;&lt;code&gt;3284258&lt;/code&gt;&lt;/a&gt;
docs: add PYTHONPATH mention for commit parser&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.1.2...v8.2.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.1.2&amp;new-version=8.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`2519474`](https://github.com/Nr18/cfn-guard-test/commit/25194748e4dfd506c82c522da15229cdc3345ce3))

* chore(deps-dev): bump urllib3 from 2.0.6 to 2.0.7 (#145)

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.0.6 to 2.0.7.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/urllib3/urllib3/releases&#34;&gt;urllib3&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;2.0.7&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;Made body stripped from HTTP requests changing the request method to
GET after HTTP 303 &amp;quot;See Other&amp;quot; redirect responses.
(GHSA-g4mx-q9vg-27p4)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/urllib3/urllib3/blob/main/CHANGES.rst&#34;&gt;urllib3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;2.0.7 (2023-10-17)&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;Made body stripped from HTTP requests changing the request method to
GET after HTTP 303 &amp;quot;See Other&amp;quot; redirect responses.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/urllib3/urllib3/commit/56f01e088dc006c03d4ee6ea9da4ab810f1ed700&#34;&gt;&lt;code&gt;56f01e0&lt;/code&gt;&lt;/a&gt;
Release 2.0.7&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/urllib3/urllib3/commit/4e50fbc5db74e32cabd5ccc1ab81fc103adfe0b3&#34;&gt;&lt;code&gt;4e50fbc&lt;/code&gt;&lt;/a&gt;
Merge pull request from GHSA-g4mx-q9vg-27p4&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/urllib3/urllib3/commit/80808b04bfa68fbd099828848c96ee25df185f1d&#34;&gt;&lt;code&gt;80808b0&lt;/code&gt;&lt;/a&gt;
Fix docs build on Python 3.12 (&lt;a
href=&#34;https://redirect.github.com/urllib3/urllib3/issues/3144&#34;&gt;#3144&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/urllib3/urllib3/commit/f28deff1cf162c673b50d88d3552e91bda6d68a8&#34;&gt;&lt;code&gt;f28deff&lt;/code&gt;&lt;/a&gt;
Add 1.26.17 to the current changelog&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/urllib3/urllib3/compare/2.0.6...2.0.7&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=urllib3&amp;package-manager=pip&amp;previous-version=2.0.6&amp;new-version=2.0.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/cfn-guard-test/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`e2caf3d`](https://github.com/Nr18/cfn-guard-test/commit/e2caf3d6ad8ff9fac87ae12ae4ba57b7d1cc1fef))

* chore(deps-dev): bump black from 23.9.1 to 23.10.0 (#144)

Bumps [black](https://github.com/psf/black) from 23.9.1 to 23.10.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix comments getting removed from inside parenthesized strings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3909&#34;&gt;#3909&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix long lines with power operators getting split before the line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Long type hints are now wrapped in parentheses and properly indented
when split across
multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Magic trailing commas are now respected in return types. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Require one empty line after module-level docstrings. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Treat raw triple-quoted strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix cache versioning logic when &lt;code&gt;BLACK_CACHE_DIR&lt;/code&gt; is set
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3937&#34;&gt;#3937&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where attributes named &lt;code&gt;type&lt;/code&gt; were not acccepted
inside &lt;code&gt;match&lt;/code&gt; statements
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3950&#34;&gt;#3950&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for PEP 695 type aliases containing lambdas and other
unusual expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black no longer attempts to provide special errors for attempting to
format Python 2
code (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3933&#34;&gt;#3933&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Black will more consistently print stacktraces on internal errors in
verbose mode
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The action output displayed in the job summary is now wrapped in
Markdown (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3914&#34;&gt;#3914&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix comments getting removed from inside parenthesized strings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3909&#34;&gt;#3909&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix long lines with power operators getting split before the line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Long type hints are now wrapped in parentheses and properly indented
when split across
multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Magic trailing commas are now respected in return types. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Require one empty line after module-level docstrings. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Treat raw triple-quoted strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix cache versioning logic when &lt;code&gt;BLACK_CACHE_DIR&lt;/code&gt; is set
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3937&#34;&gt;#3937&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where attributes named &lt;code&gt;type&lt;/code&gt; were not acccepted
inside &lt;code&gt;match&lt;/code&gt; statements
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3950&#34;&gt;#3950&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for PEP 695 type aliases containing lambdas and other
unusual expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black no longer attempts to provide special errors for attempting to
format Python 2
code (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3933&#34;&gt;#3933&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Black will more consistently print stacktraces on internal errors in
verbose mode
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The action output displayed in the job summary is now wrapped in
Markdown (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3914&#34;&gt;#3914&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/9edba85f71d50d12996ef7bda576426362016171&#34;&gt;&lt;code&gt;9edba85&lt;/code&gt;&lt;/a&gt;
Prepare release 23.10.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3951&#34;&gt;#3951&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/bb588073ab286a9f1f8d839ab2cebe13011dd22c&#34;&gt;&lt;code&gt;bb58807&lt;/code&gt;&lt;/a&gt;
Fix parser bug where &amp;quot;type&amp;quot; was misinterpreted as a keyword
inside a match (#...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/722735d20ebdc66c0da0e0df7658293455694500&#34;&gt;&lt;code&gt;722735d&lt;/code&gt;&lt;/a&gt;
Fix grammar for type alias support (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/abe57e3d92727f1b26c717fad3978159b987fe79&#34;&gt;&lt;code&gt;abe57e3&lt;/code&gt;&lt;/a&gt;
Treat raw strings like other docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1648ac51806d092c95cb9bb2e4a5bffda6095bc1&#34;&gt;&lt;code&gt;1648ac5&lt;/code&gt;&lt;/a&gt;
Fix long lines with power operator(s) getting splitted before line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3&#34;&gt;#3&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/6f84f652850dca8a1b578581e2fbb2cb95e791cc&#34;&gt;&lt;code&gt;6f84f65&lt;/code&gt;&lt;/a&gt;
Migrate mypy config to pyproject.toml (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3936&#34;&gt;#3936&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/3bb92146f59804a6ead47d5f2d0fdc47daa6b698&#34;&gt;&lt;code&gt;3bb9214&lt;/code&gt;&lt;/a&gt;
CI Test: Deprecating &#39;Healthcheck.all()&#39; from Hypothesis in fuzz.py (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3945&#34;&gt;#3945&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/935f303a0a7b794e722c7df00c906be285884874&#34;&gt;&lt;code&gt;935f303&lt;/code&gt;&lt;/a&gt;
Fix test that was not being run (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3939&#34;&gt;#3939&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/b7717c3f1e73d6b847e2534a2cebbb657b96caf8&#34;&gt;&lt;code&gt;b7717c3&lt;/code&gt;&lt;/a&gt;
Standardise newlines after module-level docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7aa37ea0adf864baf3ef3dfbcfaf5ff1ff780250&#34;&gt;&lt;code&gt;7aa37ea&lt;/code&gt;&lt;/a&gt;
Report all stacktraces in verbose mode (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.9.1...23.10.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.9.1&amp;new-version=23.10.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`2a921a5`](https://github.com/Nr18/cfn-guard-test/commit/2a921a54fd344aa7725c650cef2f3628b268fda4))

* chore(deps-dev): bump mypy from 1.6.0 to 1.6.1 (#146)

Bumps [mypy](https://github.com/python/mypy) from 1.6.0 to 1.6.1.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/9b891fe5a101ecbb818f3f16641ab909f289ba04&#34;&gt;&lt;code&gt;9b891fe&lt;/code&gt;&lt;/a&gt;
Remove +dev from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6b6504eb8a96fa6a9c7b8f034803eb9a0444fe86&#34;&gt;&lt;code&gt;6b6504e&lt;/code&gt;&lt;/a&gt;
Fix crash on ParamSpec unification (for real) (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16259&#34;&gt;#16259&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/eb81e63e9dec4dd4c75b307871d1ef9b3e350838&#34;&gt;&lt;code&gt;eb81e63&lt;/code&gt;&lt;/a&gt;
Fix crash on ParamSpec unification (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16251&#34;&gt;#16251&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/45f7a12e558e4a48446af3b36494dcb4045c1028&#34;&gt;&lt;code&gt;45f7a12&lt;/code&gt;&lt;/a&gt;
Add +dev to version&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.6.0...v1.6.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.6.0&amp;new-version=1.6.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`4bdd97e`](https://github.com/Nr18/cfn-guard-test/commit/4bdd97ead0c9d363704893f0fab4e266cbfc3fc2))

* chore: tweak dependabot ([`849ef64`](https://github.com/Nr18/cfn-guard-test/commit/849ef644f4de5f067476ad2267f5044cbf7b5a04))

* chore(deps-dev): bump python-semantic-release from 8.1.1 to 8.1.2 (#143)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 8.1.1 to 8.1.2.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.1.2 (2023-10-13)&lt;/h1&gt;
&lt;h2&gt;Build&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): update importlib-resources requirement (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/719&#34;&gt;#719&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/b1ec8fed0047c79e85fd986cdbd246d2325e2b7f&#34;&gt;&lt;code&gt;b1ec8fe&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): bump ruff from 0.0.290 to 0.0.292 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/726&#34;&gt;#726&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9818cb0066ff27adb8d24cdee4ed714754c32e5e&#34;&gt;&lt;code&gt;9818cb0&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Chore&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;chore: remove setup.py as setuptools no longer needs it (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/d8762c8d4e9772f4ba016116a28948af4a4ee4d6&#34;&gt;&lt;code&gt;d8762c8&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;chore: clearer pytest output from tox (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/d890e466d2dad0538ceb58932b987abbd662fafc&#34;&gt;&lt;code&gt;d890e46&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;chore: pre-commit autoupdate &amp;amp;&amp;amp; pre-commit run -a (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/7f448f20ef207f0314c63f94f055f8285064df16&#34;&gt;&lt;code&gt;7f448f2&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;chore: add tests for python 3.12 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/728&#34;&gt;#728&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/42360fd93975f9ec4e1784dcd4b4cec23acc5de4&#34;&gt;&lt;code&gt;42360fd&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Fix&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;fix: correct lint errors&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;GitHub.upload_asset now raises ValueError instead of
requests.HTTPError (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/a13a6c37e180dc422599939a5725835306c18ff2&#34;&gt;&lt;code&gt;a13a6c3&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;fix: Error when running build command on windows systems (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/732&#34;&gt;#732&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/25536574760b407410f435441da533fafbf94402&#34;&gt;&lt;code&gt;2553657&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.1.2 (2023-10-13)&lt;/h2&gt;
&lt;h3&gt;Build&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): update importlib-resources requirement (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/719&#34;&gt;#719&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/b1ec8fed0047c79e85fd986cdbd246d2325e2b7f&#34;&gt;&lt;code&gt;b1ec8fe&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;build(deps-dev): bump ruff from 0.0.290 to 0.0.292 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/726&#34;&gt;#726&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9818cb0066ff27adb8d24cdee4ed714754c32e5e&#34;&gt;&lt;code&gt;9818cb0&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Chore&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;chore: remove setup.py as setuptools no longer needs it (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/d8762c8d4e9772f4ba016116a28948af4a4ee4d6&#34;&gt;&lt;code&gt;d8762c8&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;chore: clearer pytest output from tox (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/d890e466d2dad0538ceb58932b987abbd662fafc&#34;&gt;&lt;code&gt;d890e46&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;chore: pre-commit autoupdate &amp;amp;&amp;amp; pre-commit run -a (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/7f448f20ef207f0314c63f94f055f8285064df16&#34;&gt;&lt;code&gt;7f448f2&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;chore: add tests for python 3.12 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/728&#34;&gt;#728&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/42360fd93975f9ec4e1784dcd4b4cec23acc5de4&#34;&gt;&lt;code&gt;42360fd&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Fix&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;fix: correct lint errors&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;GitHub.upload_asset now raises ValueError instead of
requests.HTTPError (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/a13a6c37e180dc422599939a5725835306c18ff2&#34;&gt;&lt;code&gt;a13a6c3&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;fix: Error when running build command on windows systems (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/732&#34;&gt;#732&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/25536574760b407410f435441da533fafbf94402&#34;&gt;&lt;code&gt;2553657&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/78f638757ebf482f9bc110fca7cdb873265b0b7a&#34;&gt;&lt;code&gt;78f6387&lt;/code&gt;&lt;/a&gt;
8.1.2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/d8762c8d4e9772f4ba016116a28948af4a4ee4d6&#34;&gt;&lt;code&gt;d8762c8&lt;/code&gt;&lt;/a&gt;
chore: remove setup.py as setuptools no longer needs it&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/d890e466d2dad0538ceb58932b987abbd662fafc&#34;&gt;&lt;code&gt;d890e46&lt;/code&gt;&lt;/a&gt;
chore: clearer pytest output from tox&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/7f448f20ef207f0314c63f94f055f8285064df16&#34;&gt;&lt;code&gt;7f448f2&lt;/code&gt;&lt;/a&gt;
chore: pre-commit autoupdate &amp;amp;&amp;amp; pre-commit run -a&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/a13a6c37e180dc422599939a5725835306c18ff2&#34;&gt;&lt;code&gt;a13a6c3&lt;/code&gt;&lt;/a&gt;
fix: correct lint errors&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/b1ec8fed0047c79e85fd986cdbd246d2325e2b7f&#34;&gt;&lt;code&gt;b1ec8fe&lt;/code&gt;&lt;/a&gt;
build(deps-dev): update importlib-resources requirement (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/719&#34;&gt;#719&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9818cb0066ff27adb8d24cdee4ed714754c32e5e&#34;&gt;&lt;code&gt;9818cb0&lt;/code&gt;&lt;/a&gt;
build(deps-dev): bump ruff from 0.0.290 to 0.0.292 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/726&#34;&gt;#726&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/42360fd93975f9ec4e1784dcd4b4cec23acc5de4&#34;&gt;&lt;code&gt;42360fd&lt;/code&gt;&lt;/a&gt;
chore: add tests for python 3.12 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/728&#34;&gt;#728&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/25536574760b407410f435441da533fafbf94402&#34;&gt;&lt;code&gt;2553657&lt;/code&gt;&lt;/a&gt;
fix: Error when running build command on windows systems (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/732&#34;&gt;#732&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v8.1.1...v8.1.2&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=8.1.1&amp;new-version=8.1.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`0e35bac`](https://github.com/Nr18/cfn-guard-test/commit/0e35bac846283793dbd94e086d728c03962d7fa6))

* chore(deps-dev): bump mypy from 1.5.1 to 1.6.0 (#141) ([`49d68db`](https://github.com/Nr18/cfn-guard-test/commit/49d68db13ac8a51eade43074d6bff368f7b87050))

* chore(deps-dev): bump gitpython from 3.1.35 to 3.1.37 (#142) ([`d6d07f0`](https://github.com/Nr18/cfn-guard-test/commit/d6d07f0907e182a099081e3c25f42b2c1ef2877b))

* chore(deps-dev): bump urllib3 from 2.0.3 to 2.0.6 (#140) ([`4f2fcfb`](https://github.com/Nr18/cfn-guard-test/commit/4f2fcfb633732dc828b7fad43f05cd6bd068f898))

* chore(deps-dev): bump black from 23.7.0 to 23.9.1 (#138) ([`e82362a`](https://github.com/Nr18/cfn-guard-test/commit/e82362a6d416f26a88cf0ff15815146aefdc0db7))

* chore(deps): bump click from 8.1.6 to 8.1.7 (#139) ([`cb3c641`](https://github.com/Nr18/cfn-guard-test/commit/cb3c641a17ed3a261d4fec5d96871091391e0087))

* chore(deps-dev): bump radon from 5.1.0 to 6.0.1 (#137) ([`fc7cdd9`](https://github.com/Nr18/cfn-guard-test/commit/fc7cdd9ed5ac8fc1c8435a861b735b03bfd1a6ab))

* chore(deps-dev): bump xenon from 0.9.0 to 0.9.1 (#126) ([`940fd02`](https://github.com/Nr18/cfn-guard-test/commit/940fd027783f78d84d81e371a67ea57d7c405459))

* chore(deps-dev): bump mypy from 1.5.0 to 1.5.1 (#127) ([`ec12cad`](https://github.com/Nr18/cfn-guard-test/commit/ec12cad7145b87172c115dde440356d8eb66b345))

* chore(deps): bump click from 8.1.6 to 8.1.7 (#128) ([`580154b`](https://github.com/Nr18/cfn-guard-test/commit/580154b8e5323c0be8ff307f043502dad7eec104))

* chore(deps-dev): bump pytest from 7.4.0 to 7.4.2 (#133) ([`2603329`](https://github.com/Nr18/cfn-guard-test/commit/2603329ee0a442427d18d1b5ba837e370d29f0c7))

* chore(deps-dev): bump gitpython from 3.1.32 to 3.1.35 (#136) ([`b35a55e`](https://github.com/Nr18/cfn-guard-test/commit/b35a55ee591ee97f619c4cef2f55609a5ac54f05))

* chore(deps-dev): bump certifi from 2023.5.7 to 2023.7.22 (#135) ([`9f3bb7e`](https://github.com/Nr18/cfn-guard-test/commit/9f3bb7e02f9ffc0df0a4905c615d69e6bf23cdb7))

* chore(deps-dev): bump python-semantic-release from 8.0.7 to 8.1.1 (#134) ([`9144d20`](https://github.com/Nr18/cfn-guard-test/commit/9144d20b720aec83e6640dac46ff2c4043d205b8))

* chore(deps-dev): bump python-semantic-release from 8.0.4 to 8.0.7 (#129) ([`8118f73`](https://github.com/Nr18/cfn-guard-test/commit/8118f732115ff2d1d6a5df17faa4299e0585403e))

* chore(deps-dev): bump mypy from 1.4.1 to 1.5.0 (#123)

Bumps [mypy](https://github.com/python/mypy) from 1.4.1 to 1.5.0.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/2ff7c0de571d434a9a1f82fa183d32fa32999b40&#34;&gt;&lt;code&gt;2ff7c0d&lt;/code&gt;&lt;/a&gt;
[release 1.5] stubtest: Fix &lt;code&gt;__mypy-replace&lt;/code&gt; false positives
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15689&#34;&gt;#15689&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15751&#34;&gt;#15751&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/373b73abeb14fdd1f3021f4c27fe1721d2986ed4&#34;&gt;&lt;code&gt;373b73a&lt;/code&gt;&lt;/a&gt;
[Release 1.5] Update typing_extensions stubs (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15745&#34;&gt;#15745&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/a6bd80ed8c91138ce6112b5ce71fc406d426cd01&#34;&gt;&lt;code&gt;a6bd80e&lt;/code&gt;&lt;/a&gt;
Remove &lt;code&gt;+dev&lt;/code&gt; from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/9dd0d396e0a8b477e4bf723a6a24d82db7785ea8&#34;&gt;&lt;code&gt;9dd0d39&lt;/code&gt;&lt;/a&gt;
Manually revert &amp;quot;Add support for attrs.fields (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15021&#34;&gt;#15021&lt;/a&gt;)&amp;quot;
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15674&#34;&gt;#15674&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/45e1bf7a83686a5b933eb009447e89e5d1c41ca9&#34;&gt;&lt;code&gt;45e1bf7&lt;/code&gt;&lt;/a&gt;
Typeshed cherry-pick: Fix &lt;a
href=&#34;https://github.com/patch&#34;&gt;&lt;code&gt;@​patch&lt;/code&gt;&lt;/a&gt; when
&lt;code&gt;new&lt;/code&gt; is missing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/10459&#34;&gt;#10459&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15673&#34;&gt;#15673&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/7a9418356082092d2cb1585acb816b2074cff43e&#34;&gt;&lt;code&gt;7a94183&lt;/code&gt;&lt;/a&gt;
Fix dataclass/protocol crash on joining types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15629&#34;&gt;#15629&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/2ebd51e881490f4d20635cde92ef9e3edbbad68c&#34;&gt;&lt;code&gt;2ebd51e&lt;/code&gt;&lt;/a&gt;
Teach &lt;code&gt;stubgen&lt;/code&gt; to work with &lt;code&gt;complex&lt;/code&gt; and unary
expressions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15661&#34;&gt;#15661&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/39833810ddcd29561f3ffed44703380aa26a68be&#34;&gt;&lt;code&gt;3983381&lt;/code&gt;&lt;/a&gt;
Fix testLiteralMeets failure (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15659&#34;&gt;#15659&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3bf85217386806b0f68bf8857b61379ae2f6ad1e&#34;&gt;&lt;code&gt;3bf8521&lt;/code&gt;&lt;/a&gt;
Consistently avoid type-checking unreachable code (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15386&#34;&gt;#15386&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/dfea43ff96976435ee5f37d1294cca792b8f26cf&#34;&gt;&lt;code&gt;dfea43f&lt;/code&gt;&lt;/a&gt;
Add error code &amp;quot;explicit-override&amp;quot; for strict &lt;a
href=&#34;https://github.com/override&#34;&gt;&lt;code&gt;@​override&lt;/code&gt;&lt;/a&gt; mode (PEP
698) (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15512&#34;&gt;#15512&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.4.1...v1.5.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.4.1&amp;new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`57b5441`](https://github.com/Nr18/cfn-guard-test/commit/57b5441d4c915e01630387ab89afce5b518c7897))

* chore(deps): bump the dependencies group with 1 update (#122)

Bumps the dependencies group with 1 update:
[click](https://github.com/pallets/click).

&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/releases&#34;&gt;click&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.1.6&lt;/h2&gt;
&lt;p&gt;This is a fix release for the 8.1.x feature branch. If you were
having issues with type checking tools like pyright or mypy not
accepting uses of Click&#39;s decorators, this should fix that.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Changes: &lt;a
href=&#34;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-6&#34;&gt;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-6&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Milestone: &lt;a
href=&#34;https://github.com/pallets/click/milestone/21?closed=1&#34;&gt;https://github.com/pallets/click/milestone/21?closed=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;8.1.5&lt;/h2&gt;
&lt;p&gt;This is a fix release for the 8.1.x feature branch. This fixes an
issue with decorator type annotations that caused type checkers to fail
for valid code. There are no runtime behavior changes.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Changes: &lt;a
href=&#34;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-5&#34;&gt;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-5&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Milestone: &lt;a
href=&#34;https://github.com/pallets/click/milestone/20?closed=1&#34;&gt;https://github.com/pallets/click/milestone/20?closed=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/blob/8.1.6/CHANGES.rst&#34;&gt;click&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;Version 8.1.6&lt;/h2&gt;
&lt;p&gt;Released 2023-07-18&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fix an issue with type hints for &lt;code&gt;@click.group()&lt;/code&gt;.
:issue:&lt;code&gt;2558&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Version 8.1.5&lt;/h2&gt;
&lt;p&gt;Released 2023-07-13&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fix an issue with type hints for &lt;code&gt;@click.command()&lt;/code&gt;,
&lt;code&gt;@click.option()&lt;/code&gt;, and
other decorators. Introduce typing tests. :issue:&lt;code&gt;2558&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/3793f5b2d79d5999552b970bf17c37588efcf008&#34;&gt;&lt;code&gt;3793f5b&lt;/code&gt;&lt;/a&gt;
release version 8.1.6&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/1a15373bf35e004dbf31826df8d7fe1765aafb77&#34;&gt;&lt;code&gt;1a15373&lt;/code&gt;&lt;/a&gt;
Fix &lt;code&gt;group&lt;/code&gt; overload (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2565&#34;&gt;#2565&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/20280d4f76928db0617fbc4c0059fabb42b8d77e&#34;&gt;&lt;code&gt;20280d4&lt;/code&gt;&lt;/a&gt;
fix &lt;code&gt;group&lt;/code&gt; overload with &lt;code&gt;cls&lt;/code&gt; arg&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/56b15be8b843a26a8065c65f8a208eef7b7c05bc&#34;&gt;&lt;code&gt;56b15be&lt;/code&gt;&lt;/a&gt;
start version 8.1.6&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/aca9f753afd9877ae8ee86609ace18eadf3ea116&#34;&gt;&lt;code&gt;aca9f75&lt;/code&gt;&lt;/a&gt;
release version 8.1.5 (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2564&#34;&gt;#2564&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/63c171612889102dfae5f7270be78b567cf4251b&#34;&gt;&lt;code&gt;63c1716&lt;/code&gt;&lt;/a&gt;
release version 8.1.5&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/449d38f517845f39b0ffd4df64f90403933b0e0e&#34;&gt;&lt;code&gt;449d38f&lt;/code&gt;&lt;/a&gt;
Fix types, introduce type tests (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2562&#34;&gt;#2562&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/d17dbc2c0faee0017ea2c8d2260e72cb71848f2f&#34;&gt;&lt;code&gt;d17dbc2&lt;/code&gt;&lt;/a&gt;
start version 8.1.5&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/f20395dfe397be7746380bd8768553ce4065752b&#34;&gt;&lt;code&gt;f20395d&lt;/code&gt;&lt;/a&gt;
release version 8.1.4 (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2557&#34;&gt;#2557&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pallets/click/compare/8.1.4...8.1.6&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=click&amp;package-manager=pip&amp;previous-version=8.1.4&amp;new-version=8.1.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`d71c628`](https://github.com/Nr18/cfn-guard-test/commit/d71c628626d97cb57ceff06ef68d6a665b927c09))

* chore: update token ([`4eec8f4`](https://github.com/Nr18/cfn-guard-test/commit/4eec8f4718e66b34a4f1b173e7569c423c6b1b39))

* chore: rename secret token ([`1832b55`](https://github.com/Nr18/cfn-guard-test/commit/1832b55ae5006d10526d1fd1a243174f18ef4d11))

* chore: group dependencies and assign code owner ([`437781c`](https://github.com/Nr18/cfn-guard-test/commit/437781ca40a10b6707681ee8e91d1e19e5370275))

* chore: fix auto-merge ([`76b2cad`](https://github.com/Nr18/cfn-guard-test/commit/76b2cad8f0840c0476e1e294a2f306a50837684d))

* chore(deps-dev): bump python-semantic-release from 8.0.3 to 8.0.4 (#121) ([`77fdee1`](https://github.com/Nr18/cfn-guard-test/commit/77fdee193cbd2b4c7e3b2d03cfdc328c99bc04fe))

* chore(deps-dev): bump python-semantic-release from 8.0.2 to 8.0.3 (#120) ([`0b84165`](https://github.com/Nr18/cfn-guard-test/commit/0b841657b049595e87bd4f9fe5cf888bc85d3195))

* chore(deps-dev): bump types-toml from 0.10.8.6 to 0.10.8.7 (#119) ([`027f6e7`](https://github.com/Nr18/cfn-guard-test/commit/027f6e758ccd0e40b86b919c42c1bc52a352756e))

* chore: trigger patch release on dependency updates ([`bc51e5e`](https://github.com/Nr18/cfn-guard-test/commit/bc51e5eb84a298e966809a2cade3fc425ad8ffd1))

* chore(deps): bump click from 8.1.4 to 8.1.6 (#115)

Bumps [click](https://github.com/pallets/click) from 8.1.4 to 8.1.6.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/releases&#34;&gt;click&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.1.6&lt;/h2&gt;
&lt;p&gt;This is a fix release for the 8.1.x feature branch. If you were
having issues with type checking tools like pyright or mypy not
accepting uses of Click&#39;s decorators, this should fix that.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Changes: &lt;a
href=&#34;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-6&#34;&gt;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-6&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Milestone: &lt;a
href=&#34;https://github.com/pallets/click/milestone/21?closed=1&#34;&gt;https://github.com/pallets/click/milestone/21?closed=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;8.1.5&lt;/h2&gt;
&lt;p&gt;This is a fix release for the 8.1.x feature branch. This fixes an
issue with decorator type annotations that caused type checkers to fail
for valid code. There are no runtime behavior changes.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Changes: &lt;a
href=&#34;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-5&#34;&gt;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-5&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Milestone: &lt;a
href=&#34;https://github.com/pallets/click/milestone/20?closed=1&#34;&gt;https://github.com/pallets/click/milestone/20?closed=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/blob/8.1.6/CHANGES.rst&#34;&gt;click&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;Version 8.1.6&lt;/h2&gt;
&lt;p&gt;Released 2023-07-18&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fix an issue with type hints for &lt;code&gt;@click.group()&lt;/code&gt;.
:issue:&lt;code&gt;2558&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Version 8.1.5&lt;/h2&gt;
&lt;p&gt;Released 2023-07-13&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fix an issue with type hints for &lt;code&gt;@click.command()&lt;/code&gt;,
&lt;code&gt;@click.option()&lt;/code&gt;, and
other decorators. Introduce typing tests. :issue:&lt;code&gt;2558&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/3793f5b2d79d5999552b970bf17c37588efcf008&#34;&gt;&lt;code&gt;3793f5b&lt;/code&gt;&lt;/a&gt;
release version 8.1.6&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/1a15373bf35e004dbf31826df8d7fe1765aafb77&#34;&gt;&lt;code&gt;1a15373&lt;/code&gt;&lt;/a&gt;
Fix &lt;code&gt;group&lt;/code&gt; overload (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2565&#34;&gt;#2565&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/20280d4f76928db0617fbc4c0059fabb42b8d77e&#34;&gt;&lt;code&gt;20280d4&lt;/code&gt;&lt;/a&gt;
fix &lt;code&gt;group&lt;/code&gt; overload with &lt;code&gt;cls&lt;/code&gt; arg&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/56b15be8b843a26a8065c65f8a208eef7b7c05bc&#34;&gt;&lt;code&gt;56b15be&lt;/code&gt;&lt;/a&gt;
start version 8.1.6&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/aca9f753afd9877ae8ee86609ace18eadf3ea116&#34;&gt;&lt;code&gt;aca9f75&lt;/code&gt;&lt;/a&gt;
release version 8.1.5 (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2564&#34;&gt;#2564&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/63c171612889102dfae5f7270be78b567cf4251b&#34;&gt;&lt;code&gt;63c1716&lt;/code&gt;&lt;/a&gt;
release version 8.1.5&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/449d38f517845f39b0ffd4df64f90403933b0e0e&#34;&gt;&lt;code&gt;449d38f&lt;/code&gt;&lt;/a&gt;
Fix types, introduce type tests (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2562&#34;&gt;#2562&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/d17dbc2c0faee0017ea2c8d2260e72cb71848f2f&#34;&gt;&lt;code&gt;d17dbc2&lt;/code&gt;&lt;/a&gt;
start version 8.1.5&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/f20395dfe397be7746380bd8768553ce4065752b&#34;&gt;&lt;code&gt;f20395d&lt;/code&gt;&lt;/a&gt;
release version 8.1.4 (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2557&#34;&gt;#2557&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pallets/click/compare/8.1.4...8.1.6&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=click&amp;package-manager=pip&amp;previous-version=8.1.4&amp;new-version=8.1.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`c8adeca`](https://github.com/Nr18/cfn-guard-test/commit/c8adeca4045123a19f1d46fe57eebdf46846b3ec))

* chore(deps-dev): bump python-semantic-release from 7.34.6 to 8.0.2 (#116)

Bumps
[python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
from 7.34.6 to 8.0.2.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/releases&#34;&gt;python-semantic-release&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;v8.0.2 (2023-07-18)&lt;/h1&gt;
&lt;h2&gt;Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;docs: correct version_toml example in migrating_from_v7.rst (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/641&#34;&gt;#641&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/325d5e048bd89cb2a94c47029d4878b27311c0f0&#34;&gt;&lt;code&gt;325d5e0&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs: clarify v8 breaking changes in GitHub action inputs (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/643&#34;&gt;#643&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/cda050cd9e789d81458157ee240ff99ec65c6f25&#34;&gt;&lt;code&gt;cda050c&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs: better description for tag_format usage (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/2129b729837eccc41a33dbb49785a8a30ce6b187&#34;&gt;&lt;code&gt;2129b72&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Fix&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;fix: handle missing configuration (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/644&#34;&gt;#644&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/f15753ce652f36cc03b108c667a26ab74bcbf95d&#34;&gt;&lt;code&gt;f15753c&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;v8.0.1 (2023-07-17)&lt;/h1&gt;
&lt;h2&gt;Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;docs: reduce readthedocs formats and add entries to migration from v7
guide (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9b6ddfef448f9de30fa2845034f76655d34a9912&#34;&gt;&lt;code&gt;9b6ddfe&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs(migration): fix hyperlink (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/631&#34;&gt;#631&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/5fbd52d7de4982b5689651201a0e07b445158645&#34;&gt;&lt;code&gt;5fbd52d&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Fix&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;fix: invalid version in Git history should not cause a release
failure (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/632&#34;&gt;#632&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/254430b5cc5f032016b4c73168f0403c4d87541e&#34;&gt;&lt;code&gt;254430b&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;v8.0.0 (2023-07-16)&lt;/h1&gt;
&lt;h2&gt;Breaking&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;feat!: v8 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/619&#34;&gt;#619&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;feat!: 8.0.x (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/538&#34;&gt;#538&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Co-authored-by: Johan &amp;lt;&lt;a
href=&#34;mailto:johanhmr@gmail.com&#34;&gt;johanhmr@gmail.com&lt;/a&gt;&amp;gt;
Co-authored-by: U-NEO\johan &amp;lt;&lt;a
href=&#34;mailto:johan.hammar@ombea.com&#34;&gt;johan.hammar@ombea.com&lt;/a&gt;&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;fix: correct Dockerfile CLI command and GHA fetch&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix: resolve branch checkout logic in GHA&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix: remove commit amending behaviour&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;this was not working when there were no source code changes to be
made, as it lead
to attempting to amend a HEAD commit that wasn&amp;amp;&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/39&#34;&gt;#39&lt;/a&gt;;t
produced by PSR&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;8.0.0-alpha.1&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Automatically generated by python-semantic-release&lt;/p&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md&#34;&gt;python-semantic-release&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;v8.0.2 (2023-07-18)&lt;/h2&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;docs: correct version_toml example in migrating_from_v7.rst (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/641&#34;&gt;#641&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/325d5e048bd89cb2a94c47029d4878b27311c0f0&#34;&gt;&lt;code&gt;325d5e0&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs: clarify v8 breaking changes in GitHub action inputs (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/643&#34;&gt;#643&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/cda050cd9e789d81458157ee240ff99ec65c6f25&#34;&gt;&lt;code&gt;cda050c&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs: better description for tag_format usage (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/2129b729837eccc41a33dbb49785a8a30ce6b187&#34;&gt;&lt;code&gt;2129b72&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Fix&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;fix: handle missing configuration (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/644&#34;&gt;#644&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/f15753ce652f36cc03b108c667a26ab74bcbf95d&#34;&gt;&lt;code&gt;f15753c&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;v8.0.1 (2023-07-17)&lt;/h2&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;docs: reduce readthedocs formats and add entries to migration from v7
guide (&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9b6ddfef448f9de30fa2845034f76655d34a9912&#34;&gt;&lt;code&gt;9b6ddfe&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;docs(migration): fix hyperlink (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/631&#34;&gt;#631&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/5fbd52d7de4982b5689651201a0e07b445158645&#34;&gt;&lt;code&gt;5fbd52d&lt;/code&gt;&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Fix&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;fix: invalid version in Git history should not cause a release
failure (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/632&#34;&gt;#632&lt;/a&gt;)
(&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/254430b5cc5f032016b4c73168f0403c4d87541e&#34;&gt;&lt;code&gt;254430b&lt;/code&gt;&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;v8.0.0 (2023-07-16)&lt;/h2&gt;
&lt;h3&gt;Breaking&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;feat!: v8 (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/619&#34;&gt;#619&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;feat!: 8.0.x (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/538&#34;&gt;#538&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;Co-authored-by: Johan &amp;lt;&lt;a
href=&#34;mailto:johanhmr@gmail.com&#34;&gt;johanhmr@gmail.com&lt;/a&gt;&amp;gt;
Co-authored-by: U-NEO\johan &amp;lt;&lt;a
href=&#34;mailto:johan.hammar@ombea.com&#34;&gt;johan.hammar@ombea.com&lt;/a&gt;&amp;gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;fix: correct Dockerfile CLI command and GHA fetch&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix: resolve branch checkout logic in GHA&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;fix: remove commit amending behaviour&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;this was not working when there were no source code changes to be
made, as it lead
to attempting to amend a HEAD commit that wasn&amp;amp;&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/39&#34;&gt;#39&lt;/a&gt;;t
produced by PSR&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;8.0.0-alpha.1&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/8950c5236099151e13cfd1ea9dae8e8c2477221b&#34;&gt;&lt;code&gt;8950c52&lt;/code&gt;&lt;/a&gt;
8.0.2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/f15753ce652f36cc03b108c667a26ab74bcbf95d&#34;&gt;&lt;code&gt;f15753c&lt;/code&gt;&lt;/a&gt;
fix: handle missing configuration (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/644&#34;&gt;#644&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/325d5e048bd89cb2a94c47029d4878b27311c0f0&#34;&gt;&lt;code&gt;325d5e0&lt;/code&gt;&lt;/a&gt;
docs: correct version_toml example in migrating_from_v7.rst (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/641&#34;&gt;#641&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/cda050cd9e789d81458157ee240ff99ec65c6f25&#34;&gt;&lt;code&gt;cda050c&lt;/code&gt;&lt;/a&gt;
docs: clarify v8 breaking changes in GitHub action inputs (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/643&#34;&gt;#643&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/2129b729837eccc41a33dbb49785a8a30ce6b187&#34;&gt;&lt;code&gt;2129b72&lt;/code&gt;&lt;/a&gt;
docs: better description for tag_format usage&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/0244086493441a32e66698a034595360a19574bb&#34;&gt;&lt;code&gt;0244086&lt;/code&gt;&lt;/a&gt;
8.0.1&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/254430b5cc5f032016b4c73168f0403c4d87541e&#34;&gt;&lt;code&gt;254430b&lt;/code&gt;&lt;/a&gt;
fix: invalid version in Git history should not cause a release failure
(&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/632&#34;&gt;#632&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/9b6ddfef448f9de30fa2845034f76655d34a9912&#34;&gt;&lt;code&gt;9b6ddfe&lt;/code&gt;&lt;/a&gt;
docs: reduce readthedocs formats and add entries to migration from v7
guide&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/5fbd52d7de4982b5689651201a0e07b445158645&#34;&gt;&lt;code&gt;5fbd52d&lt;/code&gt;&lt;/a&gt;
docs(migration): fix hyperlink (&lt;a
href=&#34;https://redirect.github.com/python-semantic-release/python-semantic-release/issues/631&#34;&gt;#631&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/commit/03f89dd88a62e1a66e604c040681a25da9d3fd3a&#34;&gt;&lt;code&gt;03f89dd&lt;/code&gt;&lt;/a&gt;
8.0.0&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python-semantic-release/python-semantic-release/compare/v7.34.6...v8.0.2&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-semantic-release&amp;package-manager=pip&amp;previous-version=7.34.6&amp;new-version=8.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`f120005`](https://github.com/Nr18/cfn-guard-test/commit/f1200059d5476086aaff9d7175343ed0521f4def))

* chore: change license to apache 2.0 ([`f765cca`](https://github.com/Nr18/cfn-guard-test/commit/f765ccafd6d0d4eb5b900db02b42dc2ac5a7aebd))

* chore: enable auto-commit for dependabot pull requests (#117)

**Issue #, if available:**

## Description of changes:

&lt;!--- One or two sentences as a summary of what&#39;s being changed --&gt;

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [ ] Update tests
* [ ] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`4038453`](https://github.com/Nr18/cfn-guard-test/commit/4038453791b1c99ecb7e4767ab8d03d6ca065afc))

* chore(deps): bump click from 8.1.4 to 8.1.5 (#111) ([`568a63a`](https://github.com/Nr18/cfn-guard-test/commit/568a63aa9143a2e4e887352f5aeac5a05573ff75))

### Feature

* feat: support cfn-guard v3.x.x (#168)

**Issue #, if available:**

## Description of changes:

When cfn-guard 3.x.x was released the output format has changed.
Previously the rule name was encapsulated in quotes. With the new
release this was removed but the cfn-guard-test wrapper still expected
these quotes.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [ ] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`250e7b9`](https://github.com/Nr18/cfn-guard-test/commit/250e7b9be0f06f7a50d45332a0f99da236f0af46))

### Fix

* fix: trigger release ([`7a86b1d`](https://github.com/Nr18/cfn-guard-test/commit/7a86b1d66b455e0cf21ffa01bbf194b942cfa5b6))

### Unknown

* Update auto-merge.yml ([`2da6485`](https://github.com/Nr18/cfn-guard-test/commit/2da64855361185532962697f0920bfab418b21bd))

* Update dependabot.yml ([`d4fe840`](https://github.com/Nr18/cfn-guard-test/commit/d4fe840c81cc830a33522bfce586b9534b4b5be4))


## v0.7.1 (2023-07-12)

### Chore

* chore(deps-dev): bump black from 23.3.0 to 23.7.0 (#109) ([`a341282`](https://github.com/Nr18/cfn-guard-test/commit/a34128279b6c7dc9e9e8d790629cc6364843f127))

* chore(deps): bump click from 8.1.3 to 8.1.4 (#107) ([`af7e8ae`](https://github.com/Nr18/cfn-guard-test/commit/af7e8ae09ae7ab0cb8a38291133aa9676781030f))

* chore(deps-dev): bump mypy from 1.4.0 to 1.4.1 (#106) ([`2e5056a`](https://github.com/Nr18/cfn-guard-test/commit/2e5056acd1fa820374e7dc97e89f01b86488e380))

* chore(deps-dev): bump pytest from 7.3.2 to 7.4.0 (#105) ([`3173ffb`](https://github.com/Nr18/cfn-guard-test/commit/3173ffbcbc86be290e31d5d90bd648268718c51d))

* chore(deps-dev): bump mypy from 1.3.0 to 1.4.0 (#104) ([`016b469`](https://github.com/Nr18/cfn-guard-test/commit/016b46948ed1bab400cf0914dbf558bf24b4df7f))

* chore(deps-dev): bump python-semantic-release from 7.34.4 to 7.34.6 (#103) ([`86027fc`](https://github.com/Nr18/cfn-guard-test/commit/86027fcbd00148601807315a0cfcd9750f3f2218))

### Fix

* fix: update dependencies (#110)

**Issue #, if available:**

## Description of changes:

&lt;!--- One or two sentences as a summary of what&#39;s being changed --&gt;

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`6c7a099`](https://github.com/Nr18/cfn-guard-test/commit/6c7a0993717450cdfbb47c50784d685a83d19de1))


## v0.7.0 (2023-06-15)

### Chore

* chore(deps-dev): bump pytest from 7.3.1 to 7.3.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.1 to 7.3.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.1...7.3.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8eaaddf`](https://github.com/Nr18/cfn-guard-test/commit/8eaaddf253b20243db94e263ed90e9f45f1b26e5))

* chore(deps): bump cryptography from 39.0.2 to 41.0.0

Bumps [cryptography](https://github.com/pyca/cryptography) from 39.0.2 to 41.0.0.
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/39.0.2...41.0.0)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cef0c6d`](https://github.com/Nr18/cfn-guard-test/commit/cef0c6d498212a3c6ebea2508fa85fa0a334d9a6))

* chore(deps-dev): bump mypy from 1.2.0 to 1.3.0

Bumps [mypy](https://github.com/python/mypy) from 1.2.0 to 1.3.0.
- [Commits](https://github.com/python/mypy/compare/v1.2.0...v1.3.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4311aae`](https://github.com/Nr18/cfn-guard-test/commit/4311aae611dce49673b56d02fab5df5732adda89))

* chore(deps-dev): bump pytest-cov from 4.0.0 to 4.1.0

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 4.0.0 to 4.1.0.
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v4.0.0...v4.1.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`109e317`](https://github.com/Nr18/cfn-guard-test/commit/109e3170e5eefa48799ada97698eedab32610403))

* chore(deps): bump requests from 2.28.2 to 2.31.0

Bumps [requests](https://github.com/psf/requests) from 2.28.2 to 2.31.0.
- [Release notes](https://github.com/psf/requests/releases)
- [Changelog](https://github.com/psf/requests/blob/main/HISTORY.md)
- [Commits](https://github.com/psf/requests/compare/v2.28.2...v2.31.0)

---
updated-dependencies:
- dependency-name: requests
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b9310cf`](https://github.com/Nr18/cfn-guard-test/commit/b9310cfa19f04497a56482b248ec2c4b851ff2f8))

* chore(deps-dev): bump pytest from 7.3.0 to 7.3.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.0 to 7.3.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.0...7.3.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b206a0f`](https://github.com/Nr18/cfn-guard-test/commit/b206a0fe1a97878099e64dac820b13bc5e3d2424))

* chore(deps-dev): bump pytest from 7.2.2 to 7.3.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.2 to 7.3.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.2...7.3.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cecf7e8`](https://github.com/Nr18/cfn-guard-test/commit/cecf7e8ef73c0da008c6d05a2e99ce02db925f71))

* chore(deps-dev): bump mypy from 1.1.1 to 1.2.0

Bumps [mypy](https://github.com/python/mypy) from 1.1.1 to 1.2.0.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v1.1.1...v1.2.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7dbf9e7`](https://github.com/Nr18/cfn-guard-test/commit/7dbf9e70adf9598f12b3ec5598d4d1657bc1246a))

* chore(deps-dev): bump black from 23.1.0 to 23.3.0

Bumps [black](https://github.com/psf/black) from 23.1.0 to 23.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.1.0...23.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ca641cf`](https://github.com/Nr18/cfn-guard-test/commit/ca641cf8cc6c6bf1cdff6a612b39b3ce98db4b0e))

* chore(deps-dev): bump types-toml from 0.10.8.5 to 0.10.8.6

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8.5 to 0.10.8.6.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0f860c4`](https://github.com/Nr18/cfn-guard-test/commit/0f860c4c67da11238e77e60899c4a72ab5a7f020))

* chore(deps-dev): bump mypy from 1.0.1 to 1.1.1

Bumps [mypy](https://github.com/python/mypy) from 1.0.1 to 1.1.1.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v1.0.1...v1.1.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ac8d916`](https://github.com/Nr18/cfn-guard-test/commit/ac8d9160c3af7fda05770aa567f0d343d3c1f052))

* chore: version bump (#87) ([`14dc342`](https://github.com/Nr18/cfn-guard-test/commit/14dc34242061db7d0d911c28087d9b27ab068a11))

* chore(deps-dev): bump types-toml from 0.10.8.4 to 0.10.8.5 (#86) ([`98f7a32`](https://github.com/Nr18/cfn-guard-test/commit/98f7a32d84b22b86e83cfc288f28fbbee21a7231))

* chore(deps-dev): bump mypy from 1.0.0 to 1.0.1 (#85) ([`785d069`](https://github.com/Nr18/cfn-guard-test/commit/785d069fde5f0dfa3c7d24524d8cb206b7f0842d))

* chore(deps-dev): bump types-toml from 0.10.8.3 to 0.10.8.4 (#84) ([`a51abc1`](https://github.com/Nr18/cfn-guard-test/commit/a51abc1b87c19af8d6f04559d34c78e49171fabb))

* chore(deps-dev): bump types-toml from 0.10.8.2 to 0.10.8.3 (#83) ([`bcdcc3e`](https://github.com/Nr18/cfn-guard-test/commit/bcdcc3ef22c5e85a1fd0f2a2c97deb0f4e43ef92))

* chore(deps-dev): bump mypy from 0.991 to 1.0.0 (#82) ([`181ce53`](https://github.com/Nr18/cfn-guard-test/commit/181ce534d7ff0ba8442e60f2c3056de6554fcbae))

* chore(deps): bump cryptography from 39.0.0 to 39.0.1 (#81) ([`0923d45`](https://github.com/Nr18/cfn-guard-test/commit/0923d452858be6201f78451fce99aea292cf3ec3))

* chore(deps-dev): bump types-toml from 0.10.8.1 to 0.10.8.2 (#80) ([`3248c4d`](https://github.com/Nr18/cfn-guard-test/commit/3248c4d087620edc80e60fec770ed083a89a6271))

* chore(deps-dev): bump black from 22.12.0 to 23.1.0 (#79) ([`0a32b25`](https://github.com/Nr18/cfn-guard-test/commit/0a32b258080c811432c111e0841e25090764c8be))

* chore(deps-dev): bump pytest from 7.2.0 to 7.2.1 (#78)

* chore(deps-dev): bump pytest from 7.2.0 to 7.2.1
* fix: update lock file
* fix: update poetry image version

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.0 to 7.2.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.0...7.2.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Joris Conijn &lt;joris@conijnonline.nl&gt; ([`0cc01fa`](https://github.com/Nr18/cfn-guard-test/commit/0cc01fa4d4acc98004e5be0f4b0bac0e3ae162ac))

* chore(deps-dev): bump pytest-mypy from 0.10.2 to 0.10.3

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.10.2 to 0.10.3.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/realpython/pytest-mypy/blob/main/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.10.2...v0.10.3)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9eb7a8a`](https://github.com/Nr18/cfn-guard-test/commit/9eb7a8aebd8f8ce182e786abc3d916305bcb795a))

* chore(deps-dev): bump black from 22.10.0 to 22.12.0

Bumps [black](https://github.com/psf/black) from 22.10.0 to 22.12.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.10.0...22.12.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`13f5f3b`](https://github.com/Nr18/cfn-guard-test/commit/13f5f3b8c6574d4163c69a6b293ecdd2acdb06bf))

* chore(deps): bump certifi from 2021.10.8 to 2022.12.7

Bumps [certifi](https://github.com/certifi/python-certifi) from 2021.10.8 to 2022.12.7.
- [Release notes](https://github.com/certifi/python-certifi/releases)
- [Commits](https://github.com/certifi/python-certifi/compare/2021.10.08...2022.12.07)

---
updated-dependencies:
- dependency-name: certifi
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4db4fbd`](https://github.com/Nr18/cfn-guard-test/commit/4db4fbd25a691f0bf5278f579a59b5c86cfd6ab5))

* chore(deps-dev): bump pytest-mypy from 0.10.1 to 0.10.2

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.10.1 to 0.10.2.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/realpython/pytest-mypy/blob/main/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.10.1...v0.10.2)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`44642cb`](https://github.com/Nr18/cfn-guard-test/commit/44642cb243c721356af7bd300caa60b1907c32a0))

* chore(deps-dev): bump twine from 4.0.1 to 4.0.2

Bumps [twine](https://github.com/pypa/twine) from 4.0.1 to 4.0.2.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/4.0.1...4.0.2)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1663f3c`](https://github.com/Nr18/cfn-guard-test/commit/1663f3c47d585fa107a887db8562fbf33cd3298b))

* chore(deps-dev): bump mypy from 0.990 to 0.991

Bumps [mypy](https://github.com/python/mypy) from 0.990 to 0.991.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.990...v0.991)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f318d35`](https://github.com/Nr18/cfn-guard-test/commit/f318d354aba85b1d88b321c981d79a6573bf9b56))

* chore(deps-dev): bump types-toml from 0.10.8 to 0.10.8.1

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.8 to 0.10.8.1.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ef3aaa0`](https://github.com/Nr18/cfn-guard-test/commit/ef3aaa05e66a4dc9accfc3a387f6553f17891285))

* chore(deps-dev): bump pytest-mypy from 0.10.0 to 0.10.1

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.10.0 to 0.10.1.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/realpython/pytest-mypy/blob/main/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.10.0...v0.10.1)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`588a6f1`](https://github.com/Nr18/cfn-guard-test/commit/588a6f10d17d2c102228ffcf89dde3debdc02fb3))

* chore(deps-dev): bump mypy from 0.982 to 0.990

Bumps [mypy](https://github.com/python/mypy) from 0.982 to 0.990.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.982...v0.990)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0988f86`](https://github.com/Nr18/cfn-guard-test/commit/0988f8682ccac8487059c0eea71ef62433d49ddd))

* chore(deps-dev): bump pytest from 7.1.3 to 7.2.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.3 to 7.2.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.3...7.2.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`fb22340`](https://github.com/Nr18/cfn-guard-test/commit/fb2234087df9f18be53ef8b1fee59f0515388ae7))

* chore(deps-dev): bump black from 22.8.0 to 22.10.0

Bumps [black](https://github.com/psf/black) from 22.8.0 to 22.10.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.8.0...22.10.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8147476`](https://github.com/Nr18/cfn-guard-test/commit/8147476b86a97a2317d2286093a2a597413d334d))

* chore(deps-dev): bump mypy from 0.981 to 0.982

Bumps [mypy](https://github.com/python/mypy) from 0.981 to 0.982.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.981...v0.982)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0d0eac4`](https://github.com/Nr18/cfn-guard-test/commit/0d0eac4523c01bb26fdab76c2849b0b00c5facc5))

* chore(deps-dev): bump pytest-mypy from 0.9.1 to 0.10.0

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.9.1 to 0.10.0.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/dbader/pytest-mypy/blob/master/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.9.1...v0.10.0)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b6c5646`](https://github.com/Nr18/cfn-guard-test/commit/b6c5646ce43ea8e471c2e88939224a8ffefbc78b))

* chore(deps-dev): bump pytest-cov from 3.0.0 to 4.0.0

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 3.0.0 to 4.0.0.
- [Release notes](https://github.com/pytest-dev/pytest-cov/releases)
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v3.0.0...v4.0.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`38a2bb5`](https://github.com/Nr18/cfn-guard-test/commit/38a2bb5018f8275a753c5f8f642906afd76b8e67))

* chore(deps-dev): bump black from 22.6.0 to 22.8.0

Bumps [black](https://github.com/psf/black) from 22.6.0 to 22.8.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.6.0...22.8.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4a6a73a`](https://github.com/Nr18/cfn-guard-test/commit/4a6a73aceb166fb10ac1c5c1b1ce283ba2658212))

* chore(deps-dev): bump mypy from 0.971 to 0.981

Bumps [mypy](https://github.com/python/mypy) from 0.971 to 0.981.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.971...v0.981)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0eeb405`](https://github.com/Nr18/cfn-guard-test/commit/0eeb40568a2836c00b9509fa91b5549dd4577145))

* chore(deps-dev): bump pytest from 7.1.2 to 7.1.3

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.2 to 7.1.3.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.2...7.1.3)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cf3f174`](https://github.com/Nr18/cfn-guard-test/commit/cf3f1747f6136f7cf8188861dd2e957a12f9e87f))

### Feature

* feat: release (#102)

**Issue #, if available:**

## Description of changes:

&lt;!--- One or two sentences as a summary of what&#39;s being changed --&gt;

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice.

---------

Co-authored-by: semantic-release &lt;semantic-release&gt; ([`d447717`](https://github.com/Nr18/cfn-guard-test/commit/d447717f6012103d3d779a00135ecc9380da7f23))

* feat: trigger release ([`4d1e369`](https://github.com/Nr18/cfn-guard-test/commit/4d1e3693557e8ee5e54ecbbb286109d2cd32d608))

### Fix

* fix: reset version ([`ac23972`](https://github.com/Nr18/cfn-guard-test/commit/ac2397204190974848001395ca67e91f401d85a2))

* fix: trigger minor release ([`31bd45a`](https://github.com/Nr18/cfn-guard-test/commit/31bd45ac5df25ec5490bf73d3a0691da09950912))

* fix: use a explicit poetry version ([`24ce8be`](https://github.com/Nr18/cfn-guard-test/commit/24ce8bef560d3ad66c49fdd8d05e802063adfc70))

### Unknown

* release trigger ([`fb88def`](https://github.com/Nr18/cfn-guard-test/commit/fb88def078be73b4d72a1ea3a49a79bf8a3257ad))

* 0.6.0 ([`43787ab`](https://github.com/Nr18/cfn-guard-test/commit/43787ab61d2f7b34bb79168e4097ac9847b9800c))

* release trigger ([`94377a1`](https://github.com/Nr18/cfn-guard-test/commit/94377a131aaab90f1cfd956db3438ca0cdc8855e))


## v0.5.0 (2022-08-26)

### Chore

* chore: version bump ([`be27639`](https://github.com/Nr18/cfn-guard-test/commit/be27639a9d4668d9b8e03231f47b362a3b6acbe3))

### Feature

* feat: improve feedback

By showing the expected and actual evaluated results. It becomes easier to see what might be incorrect with your test case. By also marking the case as failed when there are no results. We prevent incorrect assumptions that it might have passed because the results are not evaluated. ([`8805510`](https://github.com/Nr18/cfn-guard-test/commit/88055101ea61cf3f7097401bf203956bad107259))

### Unknown

* Merge pull request #60 from Nr18/develop

release 0.5.0 ([`1af70d5`](https://github.com/Nr18/cfn-guard-test/commit/1af70d5b3ef4ffc8b3bcb213972a230d779b4482))

* Merge pull request #59 from Nr18/chore/version-bump

chore: version bump ([`cb04c0f`](https://github.com/Nr18/cfn-guard-test/commit/cb04c0fdbe35176a48f64189e87816538ca35b4e))

* Merge pull request #58 from Nr18/feat/improve-feedback

feat: improve feedback ([`a8a9c11`](https://github.com/Nr18/cfn-guard-test/commit/a8a9c11837781ab6ec493bb14bb4c89cd4a9a673))


## v0.4.1 (2022-08-24)

### Chore

* chore: version bump ([`66bce9a`](https://github.com/Nr18/cfn-guard-test/commit/66bce9a5c3aedf6c7c49353efb660913f5f36cfe))

* chore(deps-dev): bump mypy from 0.961 to 0.971

Bumps [mypy](https://github.com/python/mypy) from 0.961 to 0.971.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.961...v0.971)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`03566c1`](https://github.com/Nr18/cfn-guard-test/commit/03566c1455f1ba4ddf1036bdecc4e2ee27526cb3))

* chore(deps-dev): bump types-toml from 0.10.7 to 0.10.8

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.7 to 0.10.8.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`fb4a2b8`](https://github.com/Nr18/cfn-guard-test/commit/fb4a2b8d171723c3d985c42dd5c564ab0d646cbd))

* chore(deps-dev): bump black from 22.3.0 to 22.6.0

Bumps [black](https://github.com/psf/black) from 22.3.0 to 22.6.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.3.0...22.6.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`926f8b8`](https://github.com/Nr18/cfn-guard-test/commit/926f8b8a68aa3fd78697c8ad06bd7f69f280b258))

* chore(deps-dev): bump mypy from 0.960 to 0.961

Bumps [mypy](https://github.com/python/mypy) from 0.960 to 0.961.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.960...v0.961)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6880314`](https://github.com/Nr18/cfn-guard-test/commit/68803143ebd24c6c6dc0d5fefa3b63579772b4d6))

* chore(deps-dev): bump twine from 4.0.0 to 4.0.1

Bumps [twine](https://github.com/pypa/twine) from 4.0.0 to 4.0.1.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/4.0.0...4.0.1)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6a83863`](https://github.com/Nr18/cfn-guard-test/commit/6a8386395c1b67ce8c4bb569c9b76c4f0f460332))

* chore(deps-dev): bump mypy from 0.950 to 0.960

Bumps [mypy](https://github.com/python/mypy) from 0.950 to 0.960.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.950...v0.960)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2e2e016`](https://github.com/Nr18/cfn-guard-test/commit/2e2e016ea494a47ef70a9e408799089f5620653a))

* chore(deps-dev): bump types-toml from 0.10.6 to 0.10.7

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.6 to 0.10.7.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`39d41c2`](https://github.com/Nr18/cfn-guard-test/commit/39d41c260811ec772396253d76a351b21b9111d0))

* chore(deps): bump click from 8.1.2 to 8.1.3

Bumps [click](https://github.com/pallets/click) from 8.1.2 to 8.1.3.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.2...8.1.3)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a45569a`](https://github.com/Nr18/cfn-guard-test/commit/a45569a9cbaf105ba0718098a232b8ecd87adbd9))

* chore(deps-dev): bump types-toml from 0.10.5 to 0.10.6

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.5 to 0.10.6.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a866739`](https://github.com/Nr18/cfn-guard-test/commit/a8667395af7d2eadbc433b475e909af5f38318d2))

* chore(deps): bump click from 8.1.2 to 8.1.3

Bumps [click](https://github.com/pallets/click) from 8.1.2 to 8.1.3.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.2...8.1.3)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2870117`](https://github.com/Nr18/cfn-guard-test/commit/2870117a1c8638991975d69df32b87dc2a66dcb1))

* chore(deps-dev): bump pytest from 7.1.1 to 7.1.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.1 to 7.1.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.1...7.1.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`37c0913`](https://github.com/Nr18/cfn-guard-test/commit/37c09131c145a47a5ebafae3684849a4d19edc39))

* chore(deps-dev): bump mypy from 0.942 to 0.950

Bumps [mypy](https://github.com/python/mypy) from 0.942 to 0.950.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.942...v0.950)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`bf5928f`](https://github.com/Nr18/cfn-guard-test/commit/bf5928f5c3ee1141bd140ba8884419b938ea9d30))

* chore(deps-dev): bump types-toml from 0.10.4 to 0.10.5

Bumps [types-toml](https://github.com/python/typeshed) from 0.10.4 to 0.10.5.
- [Release notes](https://github.com/python/typeshed/releases)
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-toml
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`07a5970`](https://github.com/Nr18/cfn-guard-test/commit/07a5970e98d3c617141c7ab9d34b9abe93f44796))

* chore(deps): bump click from 8.0.4 to 8.1.2

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.2.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.2)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8467341`](https://github.com/Nr18/cfn-guard-test/commit/8467341c854938b936e1cb5f1d0d8c97fc08f273))

* chore(deps): bump click from 8.0.4 to 8.1.2

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.2.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.2)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0c26e50`](https://github.com/Nr18/cfn-guard-test/commit/0c26e5054a2d6d3712f4b525c07c73a2e9affdd1))

* chore(deps): bump click from 8.0.4 to 8.1.1

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.1.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.1)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0768390`](https://github.com/Nr18/cfn-guard-test/commit/07683907008abaa996af62e6f6f49227cd861741))

* chore(deps-dev): bump twine from 3.8.0 to 4.0.0

Bumps [twine](https://github.com/pypa/twine) from 3.8.0 to 4.0.0.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/3.8.0...4.0.0)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ccd1b89`](https://github.com/Nr18/cfn-guard-test/commit/ccd1b89c13d17de0c8d35ee9ed0d5453b55a1a68))

* chore(deps-dev): bump black from 22.1.0 to 22.3.0

Bumps [black](https://github.com/psf/black) from 22.1.0 to 22.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.1.0...22.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b6dc726`](https://github.com/Nr18/cfn-guard-test/commit/b6dc72605aed0032ba04caf467bc4c67b1b44904))

* chore(deps): bump click from 8.0.4 to 8.1.0

Bumps [click](https://github.com/pallets/click) from 8.0.4 to 8.1.0.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.4...8.1.0)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`085a854`](https://github.com/Nr18/cfn-guard-test/commit/085a854f04924153dae51a8cf127969f34737c1f))

* chore(deps-dev): bump mypy from 0.941 to 0.942

Bumps [mypy](https://github.com/python/mypy) from 0.941 to 0.942.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.941...v0.942)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cc5a399`](https://github.com/Nr18/cfn-guard-test/commit/cc5a399ba43175e1dd92e6250fdb5099ce3b0886))

* chore(deps-dev): bump pytest from 7.1.0 to 7.1.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.1.0 to 7.1.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.1.0...7.1.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7a0b06e`](https://github.com/Nr18/cfn-guard-test/commit/7a0b06ef2002de7dd0aaaea616723af3d031a311))

* chore(deps-dev): bump mypy from 0.931 to 0.941

Bumps [mypy](https://github.com/python/mypy) from 0.931 to 0.941.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.931...v0.941)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`26193e0`](https://github.com/Nr18/cfn-guard-test/commit/26193e00d8bf8ec8679adf2fcb2093cf915cb1c7))

* chore(deps-dev): bump pytest from 7.0.1 to 7.1.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.0.1 to 7.1.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.0.1...7.1.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e8448b0`](https://github.com/Nr18/cfn-guard-test/commit/e8448b0ade032886e5460b92ad9529bb1462eedd))

* chore(deps-dev): bump xenon from 0.8.0 to 0.9.0

Bumps [xenon](https://github.com/rubik/xenon) from 0.8.0 to 0.9.0.
- [Release notes](https://github.com/rubik/xenon/releases)
- [Changelog](https://github.com/rubik/xenon/blob/master/CHANGELOG)
- [Commits](https://github.com/rubik/xenon/compare/v0.8.0...v0.9.0)

---
updated-dependencies:
- dependency-name: xenon
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1a32f89`](https://github.com/Nr18/cfn-guard-test/commit/1a32f8914785e338002d5d223500f264a17ea740))

### Fix

* fix: support new and old output formats

In previous versions of cfn-guard the result was shown as:

```txt
Test Case #1
Name: &#34;Rule Name&#34;
  PASS Rules:
    Rule: Expected = PASS, Evaluated = PASS
```

With newer versions they only show the `Evaluated` field when it differs from the `Expected` field. Another addition is that they show the results using brackets.

```txt
Test Case #1
Name: &#34;Rule Name&#34;
  PASS Rules:
    Rule: Expected = PASS, Evaluated = [FAIL]
``` ([`10b2497`](https://github.com/Nr18/cfn-guard-test/commit/10b2497bb57023679395a49621e628119356411b))

### Unknown

* Merge pull request #57 from Nr18/develop

release: 0.4.1 ([`b9751b8`](https://github.com/Nr18/cfn-guard-test/commit/b9751b8629a8a52b0b99e4ee52a0e29ab83e9d28))

* Merge pull request #56 from Nr18/chore/version-bump

chore: version bump ([`40153de`](https://github.com/Nr18/cfn-guard-test/commit/40153de2d08939d57a184ada55d2d4bd9ff627ea))

* Merge pull request #55 from Nr18/fix/read-evaluated-properly

fix: support new and old output formats ([`46e6c30`](https://github.com/Nr18/cfn-guard-test/commit/46e6c30679b0d4b60d243923ae9210abd6bd836d))

* Merge pull request #54 from Nr18/dependabot/pip/mypy-0.971

chore(deps-dev): bump mypy from 0.961 to 0.971 ([`fe02b14`](https://github.com/Nr18/cfn-guard-test/commit/fe02b14dd8ea40b9d6ed9750355f5dfb5c1f3713))

* Merge pull request #53 from Nr18/dependabot/pip/types-toml-0.10.8 ([`ddabeb9`](https://github.com/Nr18/cfn-guard-test/commit/ddabeb9204471ca8adb5028fcfd68826f5002774))

* Merge pull request #52 from Nr18/dependabot/pip/black-22.6.0 ([`9956b5b`](https://github.com/Nr18/cfn-guard-test/commit/9956b5b1b068071e6c5c6e0a82ada4a815e707ae))

* Merge pull request #51 from Nr18/dependabot/pip/mypy-0.961

chore(deps-dev): bump mypy from 0.960 to 0.961 ([`d7b9283`](https://github.com/Nr18/cfn-guard-test/commit/d7b92830c634c8107c8551540829b3205c757210))

* Merge pull request #50 from Nr18/dependabot/pip/twine-4.0.1 ([`59bb9ee`](https://github.com/Nr18/cfn-guard-test/commit/59bb9eee335c5cfde9c3014dbeced3b32c72b507))

* Merge pull request #49 from Nr18/dependabot/pip/mypy-0.960 ([`594490f`](https://github.com/Nr18/cfn-guard-test/commit/594490f107be46c6095ed413279939a1d336ec71))

* Merge pull request #48 from Nr18/dependabot/pip/types-toml-0.10.7

chore(deps-dev): bump types-toml from 0.10.6 to 0.10.7 ([`bbb9c5c`](https://github.com/Nr18/cfn-guard-test/commit/bbb9c5c4393b72d11d2fd7c3bb891d58e1cbf452))

* Merge pull request #47 from Nr18/dependabot/pip/click-8.1.3 ([`db5d19b`](https://github.com/Nr18/cfn-guard-test/commit/db5d19bca17507475ea2410c843dcb14b7234310))

* Merge pull request #46 from Nr18/dependabot/pip/types-toml-0.10.6 ([`bca1e8f`](https://github.com/Nr18/cfn-guard-test/commit/bca1e8f5d7c58f2035c8ea227f51cc0b610d3736))

* Merge pull request #45 from Nr18/dependabot/pip/click-8.1.3 ([`160e5ae`](https://github.com/Nr18/cfn-guard-test/commit/160e5aed4b7aa462955ec469538cddba300dc47d))

* Merge pull request #43 from Nr18/dependabot/pip/pytest-7.1.2 ([`f661a41`](https://github.com/Nr18/cfn-guard-test/commit/f661a414590f6eacae6906a1617c94fee8e6dd8a))

* Merge pull request #44 from Nr18/dependabot/pip/mypy-0.950 ([`64e5900`](https://github.com/Nr18/cfn-guard-test/commit/64e59009ad2d624b42953dfa9523851e904c178e))

* Merge pull request #42 from Nr18/dependabot/pip/types-toml-0.10.5 ([`cbb4e04`](https://github.com/Nr18/cfn-guard-test/commit/cbb4e047fac43aebb19e248c1935d5e0208d7cb6))

* Merge pull request #41 from Nr18/dependabot/pip/click-8.1.2 ([`92108d3`](https://github.com/Nr18/cfn-guard-test/commit/92108d3c397da1b618827c3439231529692cd76f))

* Merge pull request #40 from Nr18/dependabot/pip/click-8.1.2 ([`f5a4af7`](https://github.com/Nr18/cfn-guard-test/commit/f5a4af7f0fd2888f970f022f71f68373c2487a8e))

* Merge pull request #38 from Nr18/dependabot/pip/twine-4.0.0 ([`e74b561`](https://github.com/Nr18/cfn-guard-test/commit/e74b561402e4b864a1ad85016e5e0761ea98cf19))

* Merge pull request #39 from Nr18/dependabot/pip/click-8.1.1 ([`99b276d`](https://github.com/Nr18/cfn-guard-test/commit/99b276de2028db08e5b2fe3e94778f550238be0f))

* Merge pull request #37 from Nr18/dependabot/pip/black-22.3.0 ([`8504f54`](https://github.com/Nr18/cfn-guard-test/commit/8504f54c42537ca7300749717d6141310ffd467f))

* Merge pull request #35 from Nr18/dependabot/pip/click-8.1.0 ([`1e88577`](https://github.com/Nr18/cfn-guard-test/commit/1e88577791edffc4d39d15f2a74eb01f1fdb007a))

* Merge pull request #34 from Nr18/dependabot/pip/mypy-0.942 ([`97692ab`](https://github.com/Nr18/cfn-guard-test/commit/97692ab9422284c7c25d19974cb5957ee141cfe9))

* Merge pull request #33 from Nr18/dependabot/pip/pytest-7.1.1

chore(deps-dev): bump pytest from 7.1.0 to 7.1.1 ([`8324210`](https://github.com/Nr18/cfn-guard-test/commit/8324210caf2bb151075742bdb94f4f7dd4aac423))

* Merge pull request #32 from Nr18/dependabot/pip/mypy-0.941 ([`297c4d5`](https://github.com/Nr18/cfn-guard-test/commit/297c4d5a85b64408512f89202f0d211b6b1a9895))

* Merge pull request #31 from Nr18/dependabot/pip/pytest-7.1.0 ([`ae66efd`](https://github.com/Nr18/cfn-guard-test/commit/ae66efd1ff613b7ba099bac63ef4e911dc566446))

* Merge pull request #29 from Nr18/dependabot/pip/xenon-0.9.0 ([`696bc60`](https://github.com/Nr18/cfn-guard-test/commit/696bc601c302ca0ead994fcdf630347a0ae75c13))


## v0.4.0 (2022-03-07)

### Chore

* chore(deps-dev): bump mypy from 0.910 to 0.931

Bumps [mypy](https://github.com/python/mypy) from 0.910 to 0.931.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.910...v0.931)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`94d29bc`](https://github.com/Nr18/cfn-guard-test/commit/94d29bc193f6ad31c02afe3dd95f7c6002b111f2))

* chore(deps-dev): bump pytest-mypy from 0.8.1 to 0.9.1

Bumps [pytest-mypy](https://github.com/dbader/pytest-mypy) from 0.8.1 to 0.9.1.
- [Release notes](https://github.com/dbader/pytest-mypy/releases)
- [Changelog](https://github.com/dbader/pytest-mypy/blob/master/changelog.md)
- [Commits](https://github.com/dbader/pytest-mypy/compare/v0.8.1...v0.9.1)

---
updated-dependencies:
- dependency-name: pytest-mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`42397af`](https://github.com/Nr18/cfn-guard-test/commit/42397af2c9fe2feaf927cbbf24c759835dcab4a4))

* chore(deps): bump click from 8.0.3 to 8.0.4

Bumps [click](https://github.com/pallets/click) from 8.0.3 to 8.0.4.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.0.3...8.0.4)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a9e9f5e`](https://github.com/Nr18/cfn-guard-test/commit/a9e9f5ef2b68b5108955cd5b7add1f6c0f49d6e3))

* chore(deps-dev): bump pytest from 6.2.5 to 7.0.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 6.2.5 to 7.0.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/6.2.5...7.0.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`13a74c5`](https://github.com/Nr18/cfn-guard-test/commit/13a74c5b9c639f0e3810840163730ed180a2c89c))

* chore(deps-dev): bump mypy from 0.910 to 0.931

Bumps [mypy](https://github.com/python/mypy) from 0.910 to 0.931.
- [Release notes](https://github.com/python/mypy/releases)
- [Commits](https://github.com/python/mypy/compare/v0.910...v0.931)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8cb06af`](https://github.com/Nr18/cfn-guard-test/commit/8cb06af775adc79d9a0cfdeea8f117d13ce1f84c))

* chore(deps-dev): bump black from 21.12b0 to 22.1.0

Bumps [black](https://github.com/psf/black) from 21.12b0 to 22.1.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/commits/22.1.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`94985b2`](https://github.com/Nr18/cfn-guard-test/commit/94985b2c719d8e33cef840bbc06776a174672446))

* chore: version bump ([`8cf17af`](https://github.com/Nr18/cfn-guard-test/commit/8cf17af713cd7419c50a43d399e176e176b49a02))

* chore: improve release process and install dependabot

Capture the release drafter output automatically. This will simplify the release procedure. Prevent vulnerabilities by enabling dependabot. ([`428a640`](https://github.com/Nr18/cfn-guard-test/commit/428a6408103031ef4caf8d51605caaeabdee0477))

### Feature

* feat: add errors to the junit report

By adding the errors to the junit report it makes it easier to find what went happened in the CI/CD pipelines. ([`3a5cfaf`](https://github.com/Nr18/cfn-guard-test/commit/3a5cfafe5dcb434ff1bfd01ea91a4f74d4eeea89))

* feat: include the cfn-guard loading error

When cfn-guard is not capable of running a test. For example when the test yaml has an invalid format. We include the append the error message to the message fed to the wrapper. This will give additional context on what went wrong. ([`d40f1ce`](https://github.com/Nr18/cfn-guard-test/commit/d40f1cefc4ea8d0b7b1811a4805ac8c6fd543e2f))

### Fix

* fix: make mypy happy ([`6c8aad8`](https://github.com/Nr18/cfn-guard-test/commit/6c8aad842235885a09a325545e5b524ee59d0a12))

* fix: release drafter ([`07f595e`](https://github.com/Nr18/cfn-guard-test/commit/07f595e42033121cd2ede9416ca023af20327ee9))

### Unknown

* Merge pull request #28 from Nr18/develop

chore: create 0.4.0 release ([`d5ac82b`](https://github.com/Nr18/cfn-guard-test/commit/d5ac82b2f8f38d757ce998caec98ccc0585f1a47))

* Merge pull request #23 from Nr18/dependabot/pip/mypy-0.931

chore(deps-dev): bump mypy from 0.910 to 0.931 ([`aa75c02`](https://github.com/Nr18/cfn-guard-test/commit/aa75c0295d7515cd1d318d7687a5adcefa48ca00))

* Merge branch &#39;dependabot/pip/mypy-0.931&#39; of github.com:Nr18/cfn-guard-test into dependabot/pip/mypy-0.931 ([`bdc9be0`](https://github.com/Nr18/cfn-guard-test/commit/bdc9be070c9c011a72f7171587d4c12a290575ae))

* Merge pull request #26 from Nr18/dependabot/pip/pytest-mypy-0.9.1

chore(deps-dev): bump pytest-mypy from 0.8.1 to 0.9.1 ([`ffa5dbe`](https://github.com/Nr18/cfn-guard-test/commit/ffa5dbeceb227ef66f7e839a32d534ebb7b8c268))

* Merge pull request #24 from Nr18/dependabot/pip/click-8.0.4

chore(deps): bump click from 8.0.3 to 8.0.4 ([`3d29384`](https://github.com/Nr18/cfn-guard-test/commit/3d29384254c56cfdbc48d0cfbf88785d2ec3ce65))

* Merge pull request #25 from Nr18/dependabot/pip/pytest-7.0.1

chore(deps-dev): bump pytest from 6.2.5 to 7.0.1 ([`576123b`](https://github.com/Nr18/cfn-guard-test/commit/576123b77a91e2297256ea3ae8af09c69ffd2490))

* Merge pull request #22 from Nr18/dependabot/pip/black-22.1.0

chore(deps-dev): bump black from 21.12b0 to 22.1.0 ([`b1e5604`](https://github.com/Nr18/cfn-guard-test/commit/b1e5604c4794e90f5891caf3dc33144ed23b112b))

* Merge pull request #27 from Nr18/chore/version-bump

chore: version bump ([`170c9b4`](https://github.com/Nr18/cfn-guard-test/commit/170c9b4a6984bdb0705b6b4c2ad2ae128db65b65))

* Merge pull request #21 from Nr18/chore/update-release-procedure

chore: improve release process and install dependabot ([`895ed08`](https://github.com/Nr18/cfn-guard-test/commit/895ed08d66cd9e3fde3546286f2d727c3d673d9e))

* Merge pull request #20 from Nr18/feat/errors-junit

feat: add errors to the junit report ([`8dbad8b`](https://github.com/Nr18/cfn-guard-test/commit/8dbad8b549ec76b2c7e7afba69d23fc7f8afa700))

* Merge pull request #19 from Nr18/feat/add-details

feat: include the cfn-guard loading error ([`e6ec01f`](https://github.com/Nr18/cfn-guard-test/commit/e6ec01f7a18f17849dfa643b45d15fb141fde6e6))


## v0.3.0 (2022-01-29)

### Chore

* chore: version bump (#17) ([`400e086`](https://github.com/Nr18/cfn-guard-test/commit/400e0869c51ad46f27577dbafdf963d7d5587d3e))

### Feature

* feat: add support for docker (#13)

Add Dockerfile to provide an alternative installation method ([`75f6a9a`](https://github.com/Nr18/cfn-guard-test/commit/75f6a9a587ce2fc494a90446bb4c6d522c7a12ea))

### Fix

* fix: ignored tests (#16)

When you have malformed YAML tests. Or the output of `cfn-guard` could not be read. We skipped it and went to the next one. This resulted in a scenario where you might think your test ran successfully. But in reallity they where skipped.

Issue: #15 ([`67d6122`](https://github.com/Nr18/cfn-guard-test/commit/67d6122f6a4d2f2ead2d43100defaa9035b44ca2))

### Style

* style: newlines in README.md (#14)

The Markdown format officially states that titles and code fences. ([`2c2505a`](https://github.com/Nr18/cfn-guard-test/commit/2c2505ab799d9a8621dae6dc42c7c0fdb08ebb8b))

### Unknown

* Merge pull request #18 from Nr18/develop

Release 0.3.0 ([`b4f1e14`](https://github.com/Nr18/cfn-guard-test/commit/b4f1e14ef54d76cfd0d88ac766bfab4bf5358d0e))


## v0.2.0 (2021-12-23)

### Chore

* chore: release 0.2.0 #12

chore: release 0.2.0 ([`292dcc6`](https://github.com/Nr18/cfn-guard-test/commit/292dcc6e26514f80be2763873808bff873b8f58c))

* chore: version bump (#11) ([`682d7ee`](https://github.com/Nr18/cfn-guard-test/commit/682d7ee8feccfdc9b0f28704cbd37b11ce230ad4))

### Documentation

* docs: describe how to installation in venv (#5)

- describe how to install the package in a venv
- fix typo ([`fabf152`](https://github.com/Nr18/cfn-guard-test/commit/fabf1523b6e7e798ae4dd3d2275706a2ca30b1a8))

### Feature

* feat: support JUnit reporting  (#9)

* feat: support JUnit reporting

Add the ability to generate a JUnit report of the cfn-guard tests. This is useful when you want to include cfn-guard-test in a CI pipeline. ([`cc55c86`](https://github.com/Nr18/cfn-guard-test/commit/cc55c868d5be5a5b356aeaa308037fbe6f72d827))

### Fix

* fix: malformed output (#10)

When paths were supplied with a trailing slash. It resulted in two slashes in the printed path in the output.
With the introduction of JUnit reports in #9 the output was even more broken. The failure message was extended to the list but it needed to be added.

Issue: #4 and #9 ([`477f8be`](https://github.com/Nr18/cfn-guard-test/commit/477f8bef444f89c7ed94aa790aa346df703c1ac2))

### Refactor

* refactor: create a high level wrapper (#8)

By introducing a high level wrapper we have a more logical distribution in what happens where. I also added the ability to make the output a bit more verbose. And introduced time tracking of the execution. ([`9056dca`](https://github.com/Nr18/cfn-guard-test/commit/9056dcadfc526b64265dbd36be8d877f188ed0ef))

* refactor: rename method and class (#7)

Fix typo and make naming more consistent ([`9880e14`](https://github.com/Nr18/cfn-guard-test/commit/9880e14b715ee290b19df895d8661536b44d81c7))

* refactor: improve naming (#6)

Make naming simpler and consistent. ([`1034923`](https://github.com/Nr18/cfn-guard-test/commit/10349230c19b82ebe8bf127d023553a092fe93b7))


## v0.1.0 (2021-12-20)

### Chore

* chore: version bump (#1) ([`a277946`](https://github.com/Nr18/cfn-guard-test/commit/a277946a301b8e1435a2762541686a6946770ad7))

### Feature

* feat: initial commit ([`0cc50c9`](https://github.com/Nr18/cfn-guard-test/commit/0cc50c945730c39c7fbed74e5e43646fd628c48d))

### Fix

* fix: use version as tag name ([`2a54d9e`](https://github.com/Nr18/cfn-guard-test/commit/2a54d9ef43f974d90ab06dd64c3ddb2c652cae70))

### Unknown

* Merge pull request #3 from Nr18/develop

fix: use version as tag name ([`9d63f63`](https://github.com/Nr18/cfn-guard-test/commit/9d63f6301a1aa68b7887b76fdc69c83b7b02fad0))

* Merge pull request #2 from Nr18/develop

chore: version bump (#1) ([`10422ef`](https://github.com/Nr18/cfn-guard-test/commit/10422ef2aed0123bf6422db9acd85ea2a1589155))

# cookiecutter-sopel
Plugin template for Sopel 7 and higher. To use:

```sh
pip install cookiecutter
cookiecutter gh:sopel-irc/cookiecutter-sopel
```

You can then release the plugin on PyPI in the normal Python way.

Obviously, you can modify anything that the template builds, so don't feel
constrained to this one way of doing things. Please do submit PRs to this repo
if you think the template can be improved.

## Setting defaults (name, email, username)

If you find yourself creating plugins fairly often, you'll likely get tired of
typing in your name, email address, and GitHub username every time.
Fortunately, cookiecutter itself provides a way to specify default values via a
`.cookiecutterrc` file in your home directory. For example, this snippet:

```yaml
default_context:
    full_name: "dgw"
    email: "dgw@example.com"
    github_username: "dgw"
```

would override the default values for this template's `full_name`, `email`, and
`github_username` fields, meaning you could just press Enter to accept each of
these instead of retyping your info every time.

Read more [in cookiecutter's documentation][cookiecutter-user-config].

  [cookiecutter-user-config]: https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html

## Legacy module template
If you need to build a new plugin that will be compatible with Sopel 6, use the
legacy template:

```sh
pip install cookiecutter
cookiecutter gh:sopel-irc/cookiecutter-sopel --checkout sopel_modules
```

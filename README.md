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

## Legacy module template
If you need to build a new plugin that will be compatible with Sopel 6, use the
legacy template:

```sh
pip install cookiecutter
cookiecutter gh:sopel-irc/cookiecutter-sopel --checkout sopel_modules
```

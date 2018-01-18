Settings Parameters
=====================

-  .. rubric:: MATHJAX\_ENABLED
      :name: mathjax_enabled

Allow to enable/disable the mathjax app. Example:

::

    MATHJAX_ENABLED = True # to enable mathjax on your django project

-  .. rubric:: MATHJAX\_LOCAL\_PATH
      :name: mathjax_local_path

Use a local path of MathJax Library instead of the CDN. Example:

::

    MATHJAX_LOCAL_PATH = 'js/libs/mathjax/'

-  .. rubric:: MATHJAX\_CONFIG\_FILE
      :name: mathjax_config_file

Allow to configure the config file used by mathjax. Example:

::

    MATHJAX_CONFIG_FILE = "TeX-AMS-MML_HTMLorMML"

The default value is ``"TeX-AMS-MML_HTMLorMML"``.

-  .. rubric:: MATHJAX\_CONFIG\_DATA
      :name: mathjax_config_data

Allow to configure the mathjax directly by a python dictionary.
Example:

::

    MATHJAX_CONFIG_DATA = {
        "tex2jax": {
          "inlineMath":
        [
            ['$','$'],
            ['\\(','\\)']
        ]
        }
    }

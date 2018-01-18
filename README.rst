Project PyDJAX
==============
*Easily Use MathJax with Django without any hassel*

+-------------------+----------------+
| Author            | Palash Bauri   |
+===================+================+
| **version**       | |image0|       |
+-------------------+----------------+
| **Documention**   | |image1|       |
+-------------------+----------------+


**PyDjax** is an easy to use application to include MathJax in your django
projects without any hassel, and easy configure directly from django
settings.

Installation and configuration
----------------------------------

To install pydjax you can use pip::

    pip install pydjax

Then you have to add ``pydjax`` app to your ``INSTALLED_APPS`` and add a
``MATHJAX_ENABLED=True`` to your settings file.

Then you can put in any template the MathJax javascript using the
template tag mathjax\_scripts. Example::

    {% load mathjax %}
    <html>
      <head>
        <title>Sample Page</title>
        {% mathjax_scripts %}
      </head>
      <body>
        $$1+1=2$$
      </body>
    </html>

**pydjax** uses the CDN mathjax version, if you want to have your own copy
of MathJax, you have to download and put it in your static directory,
and add the ``MATHJAX_LOCAL_PATH`` with the path of MathJax on static to
your settings. Example
::

  MATHJAX_LOCAL_PATH = 'js/libs/mathjax/'

Settings Parameters
---------------------

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

.. |image0| image:: https://img.shields.io/badge/version-0.2-red.svg
.. |image1| image:: https://readthedocs.org/projects/pydjax/badge/?version=latest
	:target: http://pydjax.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

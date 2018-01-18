Installation and configuration
================================

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
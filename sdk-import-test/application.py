def application(environ, start_response):

    try:
      import globus_sdk
      response = "successfully imported globus_sdk"
    except ImportError:
      response = "could not import globus_sdk"
    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)
    return [response.encode('utf-8')]

from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'127.0.0.1:8000', 'kli.urls', name='www'),
    host(r'executives.localhost:8000', 'executives.urls', name='executives'),
    host(r'127.0.0.1:8000/membership', 'membership.urls', name='membership'),
    host(r'127.0.0.1:8000/blog', 'blog.urls', name='blog'),
    host(r'127.0.0.1:8000', 'main.urls', name='main'),
)
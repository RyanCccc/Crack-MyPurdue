HEADERS = [
    ('Content-Type', 'application/x-www-form-urlencoded'),
    ('Accept-Encoding', 'gzip, deflate'),
    ('Host', 'wl.mypurdue.purdue.edu'),
    ('Referer', 'https://wl.mypurdue.purdue.edu/cp/home/displaylogin'),
    ('User-Agent', 'Mozilla/5.0'),
]
LOGIN_URL = 'https://wl.mypurdue.purdue.edu/cp/home/login'
REGIS_CHECK_URL = 'https://wl.mypurdue.purdue.edu/' + \
    'cp/ip/login?sys=sctssb&url=' + \
    'https://selfservice.mypurdue.purdue.edu/' + \
    'prod/tzwkwbis.P_CheckAgreeAndRedir?ret_code=STU_REGSTAT'
REGIS_STATUS_CHECK_URL = 'https://selfservice.mypurdue.purdue.edu/' + \
    'prod/bwskrsta.P_RegsStatusDisp'
MAIN_URL = 'https://wl.mypurdue.purdue.edu/' + \
    'render.userLayoutRootNode.uP?uP_root=root'

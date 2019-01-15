query_check = {}

### TEST ###
query_check["cms_backend"] = '''GET services
Columns: host_name description state downtimes acknowledged
Filter: host_name ~~ tmp_srv
Filter: description ~ External_track https://cms.backendfw.xyz
Filter: description ~ CMS Connection*
Filter: description ~ NGINX cms.backendfw.xyz_access_ssl.log
Or: 3
OutputFormat: python

'''
query_check["smartfox"] = '''GET services
Columns: host_name description state downtimes acknowledged
Filter: host_name ~~ tmp_srv
Filter: description ~ Game Connection*
Filter: description ~ Process_SmartFox
Or: 2
OutputFormat: python

'''
query_check["trungop"] = '''GET services
Columns: host_name description state downtimes acknowledged
Filter: host_name ~~ tmp_srv
Filter: description ~ NGINX trungop.cf_access_ssl.log
Filter: description ~ NGINX_/var/log/nginx/trungop.cf_error_ssl.log
Or: 2
OutputFormat: python

'''

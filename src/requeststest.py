import requests
import re
r = requests.get('http://bbs.byr.cn/board/Job/mode/6?_uid=guest')
print r

str = "set([u'auth.view_group', u'auth.add_user', u'transaction.change_sender', u'myprofile.view_department', u'auth.add_permission', u'transaction.add_receiver', u'myprofile.delete_routineusers', u'transaction.change_receiver', u'sessions.change_session', u'transaction.delete_receiver', u'registration.change_registrationprofile', u'auth.view_user', u'auth.delete_permission', u'transaction.view_sender', u'myprofile.change_hrworker', u'registration.add_registrationprofile', u'admin.view_logentry', u'registration.view_registrationprofile', u'contenttypes.change_contenttype', u'myprofile.view_routineusers', u'sessions.delete_session', u'myprofile.change_department', u'myprofile.delete_hrworker', u'admin.change_logentry', u'myprofile.change_allusers', u'admin.delete_logentry', u'transaction.delete_sender', u'auth.add_group', u'myprofile.delete_department', u'myprofile.add_department', u'contenttypes.delete_contenttype', u'auth.view_permission', u'myprofile.add_allusers', u'myprofile.delete_allusers', u'auth.change_permission', u'transaction.view_receiver', u'auth.change_group', u'registration.delete_registrationprofile', u'contenttypes.view_contenttype', u'sessions.add_session', u'auth.delete_group', u'auth.delete_user', u'myprofile.view_hrworker', u'transaction.add_sender', u'myprofile.add_hrworker', u'admin.add_logentry', u'sessions.view_session', u'auth.change_user', u'myprofile.add_routineusers', u'contenttypes.add_contenttype', u'myprofile.view_allusers', u'myprofile.change_routineusers'])"
pat = re.compile('(?<=u\')([a-z]+).([a-z]+).([a-z]+)')
print pat.findall(str)
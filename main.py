from pyad import *


def ad_auth(adserver: str, login: str, passwd: str):
	pyad.set_defaults(ldap_server=adserver, username=login, password=passwd)


def ad_create_user(login: str, fname: str, lname: str, passwd: str, group: str, ad_sld: str, ad_tld: str, email: str):
	ad_group = pyad.adcontainer.from_dn("ad_group=" + group + ", dc=" + ad_sld + ", dc=" + ad_tld)
	new_user = pyad.aduser.ADUser.create(login, ad_group, password=passwd)

%global service glare

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:             openstack-%{service}
Version:          XXX
Release:          XXX
Summary:          Glare Artifact Repository
License:          ASL 2.0
URL:              https://github.com/openstack/%{service}
BuildArch:        noarch
Source0:          http://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
Source1:          %{service}.logrotate

Source10:         %{name}-api.service

BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-pbr
BuildRequires:    intltool
# Required for config generation
BuildRequires:    python-alembic
BuildRequires:    python-cursive
BuildRequires:    python-eventlet
BuildRequires:    python-futurist
BuildRequires:    python-glance-store >= 0.13.0
BuildRequires:    python-httplib2
BuildRequires:    python-jsonpatch
BuildRequires:    python-memcached
BuildRequires:    python-oslo-db
BuildRequires:    python-oslo-config >= 2:3.7.0
BuildRequires:    python-oslo-log
BuildRequires:    python-oslo-middleware >= 3.0.0
BuildRequires:    python-oslo-policy >= 0.5.0
BuildRequires:    python-oslo-utils >= 3.5.0
BuildRequires:    python-oslo-versionedobjects
BuildRequires:    python-osprofiler
BuildRequires:    python-paste-deploy
BuildRequires:    python-requests
BuildRequires:    python-routes
BuildRequires:    python-oslo-messaging >= 4.0.0
BuildRequires:    python-semantic-version
BuildRequires:    python-jwt

%description
Glare Artifact Repository


%package -n       python-%{service}
Summary:          OpenStack Glare python libraries


Requires:         python-alembic >= 0.8.7
Requires:         python-cryptography >= 1.0
Requires:         python-eventlet >= 0.18.2
Requires:         python-futurist >= 0.11.0
Requires:         python-glance-store >= 0.18.0
Requires:         python-httplib2 >= 0.7.5
Requires:         python-iso8601 >= 0.1.11
Requires:         python-jsonpatch >= 1.1
Requires:         python-jsonschema >= 2.0.0
Requires:         python-jwt >= 1.0.1
Requires:         python-keystoneauth1 >= 2.18.0
Requires:         python-keystoneclient >= 1:3.8.0
Requires:         python-keystonemiddleware >= 4.12.0
Requires:         python-memcached >= 1.54
Requires:         python-microversion-parse >= 0.1.2
Requires:         python-monotonic >= 0.6
Requires:         python-os-brick >= 1.8.0
Requires:         python-oslo-concurrency >= 3.8.0
Requires:         python-oslo-config >= 2:3.14.0
Requires:         python-oslo-context >= 2.12.0
Requires:         python-oslo-db >= 4.15.0
Requires:         python-oslo-i18n >= 2.1.0
Requires:         python-oslo-log >= 3.11.0
Requires:         python-oslo-messaging >= 5.14.0
Requires:         python-oslo-middleware >= 3.0.0
Requires:         python-oslo-policy >= 1.17.0
Requires:         python-oslo-serialization >= 1.10.0
Requires:         python-oslo-service >= 1.10.0
Requires:         python-oslo-utils >= 3.18.0
Requires:         python-oslo-versionedobjects >= 1.17.0
Requires:         python-oslo-vmware >= 0.11.1
Requires:         python-osprofiler >= 1.4.0
Requires:         python-paste
Requires:         python-paste-deploy >= 1.5.0
Requires:         python-pbr >= 1.8
Requires:         python-retrying >= 1.2.3
Requires:         python-routes >= 1.12.3
Requires:         python-semantic-version >= 2.3.1
Requires:         python-six >= 1.9.0
Requires:         python-sqlalchemy >= 1.0.10
Requires:         python-swiftclient >= 2.2.0
Requires:         python-webob >= 1.6.0
Requires:         pyOpenSSL >= 0.14

#test deps: python-mox python-nose python-requests
#test and optional store:
#ceph - glance_store.rdb
#python-boto - glance_store.s3
Requires:         python-boto

%description -n   python-glare
OpenStack Glare provides API for catalog of binary data along with its metadata.

This package contains the glare python library.

%package        common
Summary:        Components common to all OpenStack glare services

Requires:       python-glare = %{version}-%{release}

Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Requires(pre):    shadow-utils


%description    common
OpenStack Glare provides API for catalog of binary data along with its metadata.

%package        api

Summary:        OpenStack glare api

Requires:       %{name}-common = %{version}-%{release}

%description api
OpenStack Glare provides API for catalog of binary data along with its metadata.

This package contains the glare API service.


%package -n python-glare-tests
Summary:        Glare tests
Requires:       python-glare = %{version}-%{release}

%description -n python-glare-tests
OpenStack Glare provides API for catalog of binary data along with its metadata.

This package contains the Glare test files.


%prep
%setup -q -n %{service}-%{upstream_version}

find . \( -name .gitignore -o -name .placeholder \) -delete

find glare -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

rm -rf {test-,}requirements.txt tools/{pip,test}-requires


%build
# Generate config file
PYTHONPATH=. oslo-config-generator --config-file=etc/oslo-config-generator/glare.conf
%{__python2} setup.py build

# Generate oslo policies
PYTHONPATH=. oslopolicy-sample-generator --namespace=glare --output-file=etc/policy.json.sample
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

# Install config files
install -p -D -m 644 etc/glare.conf.sample %{buildroot}%{_sysconfdir}/glare/glare.conf
install -p -D -m 644 etc/policy.json.sample %{buildroot}%{_sysconfdir}/glare/policy.json
install -p -D -m 644 etc/glare-paste.ini %{buildroot}%{_sysconfdir}/glare/glare-paste.ini
install -p -D -m 644 etc/glare-swift.conf.sample %{buildroot}%{_sysconfdir}/glare/glare-swift.conf

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/glare
install -d -m 755 %{buildroot}%{_sharedstatedir}/glare/tmp
install -d -m 755 %{buildroot}%{_localstatedir}/log/glare

# Install systemd unit services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/%{name}-api.service

# Logrotate config
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Remove unused files
rm -f %{buildroot}/usr/etc/glare/*

%pre common
getent group glare >/dev/null || groupadd -r glare
if ! getent passwd glare >/dev/null; then
  useradd -r -g glare -G glare -d %{_sharedstatedir}/glare -s /sbin/nologin -c "OpenStack Glare daemon" glare
fi
exit 0

%post -n %{name}-api
%systemd_post %{name}-api.service

%preun -n %{name}-api
%systemd_preun %{name}-api.service


%files -n python-glare
%{python2_sitelib}/glare
%{python2_sitelib}/glare-*.egg-info
%exclude %{python2_sitelib}/glare_tempest_plugin

%files -n python-glare-tests
%license LICENSE
%{python2_sitelib}/glare_tempest_plugin

%files common
%doc README.rst
%dir %{_sysconfdir}/glare
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare.conf
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/policy.json
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare-paste.ini
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare-swift.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0755, glare, root)  %{_localstatedir}/log/glare

%defattr(-, glare, glare, -)
%dir %{_sharedstatedir}/glare
%dir %{_sharedstatedir}/glare/tmp

%files api
%{_bindir}/glare-api
%{_bindir}/glare-db-manage
%{_bindir}/glare-scrubber
%{_unitdir}/%{name}-api.service


%changelog

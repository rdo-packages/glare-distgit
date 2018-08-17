%global service glare

%global with_doc 1

%global common_desc \
OpenStack Glare provides API for catalog of binary data along with its metadata.

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
Source11:         %{name}-scrubber.service

BuildRequires:    git
BuildRequires:    intltool
BuildRequires:    python2-devel
BuildRequires:    python2-pbr
BuildRequires:    python2-setuptools
BuildRequires:    openstack-macros
BuildRequires:    systemd
# Required for config generation
BuildRequires:    python2-alembic
BuildRequires:    python2-cryptography
BuildRequires:    python2-cursive
BuildRequires:    python2-eventlet
BuildRequires:    python2-futurist
BuildRequires:    python2-glance-store
BuildRequires:    python-httplib2
BuildRequires:    python2-iso8601
BuildRequires:    python2-jsonpatch
BuildRequires:    python2-jsonschema
BuildRequires:    python-jwt
BuildRequires:    python2-keystoneauth1
BuildRequires:    python2-keystoneclient
BuildRequires:    python2-keystonemiddleware
BuildRequires:    python-memcached
BuildRequires:    python2-microversion-parse
BuildRequires:    python-monotonic
BuildRequires:    python2-os-brick
BuildRequires:    python2-oslo-concurrency
BuildRequires:    python2-oslo-config
BuildRequires:    python2-oslo-context
BuildRequires:    python2-oslo-db-tests
BuildRequires:    python2-oslo-i18n
BuildRequires:    python2-oslo-log
BuildRequires:    python2-oslo-messaging
BuildRequires:    python2-oslo-middleware
BuildRequires:    python2-oslo-policy
BuildRequires:    python2-oslo-serialization
BuildRequires:    python2-oslo-service
BuildRequires:    python2-oslo-utils
BuildRequires:    python2-oslo-versionedobjects
BuildRequires:    python2-oslo-vmware
BuildRequires:    python2-osprofiler
BuildRequires:    python-paste
BuildRequires:    python-paste-deploy
BuildRequires:    python2-pbr
BuildRequires:    python-retrying
BuildRequires:    python2-routes
BuildRequires:    python-semantic-version
BuildRequires:    python2-six
BuildRequires:    python2-sqlalchemy
BuildRequires:    python2-swiftclient
BuildRequires:    python2-taskflow
BuildRequires:    python-webob
BuildRequires:    python2-pyOpenSSL
# Required for tests
BuildRequires:    python2-os-testr
BuildRequires:    python2-oslotest
BuildRequires:    python2-testrepository
BuildRequires:    python2-testscenarios
BuildRequires:    python2-testtools
BuildRequires:    python2-mock
BuildRequires:    python-requests-mock

%description
Glare Artifact Repository


%package -n       python-%{service}
Summary:          OpenStack Glare python libraries


Requires:         python2-alembic >= 0.8.10
Requires:         python2-cryptography >= 1.9
Requires:         python2-eventlet >= 0.18.2
Requires:         python2-futurist >= 1.2.0
Requires:         python2-glance-store >= 0.22.0
Requires:         python-httplib2 >= 0.9.1
Requires:         python2-iso8601 >= 0.1.11
Requires:         python2-jsonpatch >= 1.16
Requires:         python2-jsonschema >= 2.6.0
Requires:         python-jwt >= 1.0.1
Requires:         python2-keystoneauth1 >= 3.3.0
Requires:         python2-keystoneclient >= 1:3.8.0
Requires:         python2-keystonemiddleware >= 4.17.0
Requires:         python-memcached >= 1.56
Requires:         python2-microversion-parse >= 0.1.2
Requires:         python-monotonic >= 0.6
Requires:         python2-os-brick >= 1.8.0
Requires:         python2-oslo-concurrency >= 3.20.0
Requires:         python2-oslo-config >= 2:5.1.0
Requires:         python2-oslo-context >= 2.19.2
Requires:         python2-oslo-db >= 4.27.0
Requires:         python2-oslo-i18n >= 3.15.3
Requires:         python2-oslo-log >= 3.30.0
Requires:         python2-oslo-messaging >= 5.29.0
Requires:         python2-oslo-middleware >= 3.31.0
Requires:         python2-oslo-policy >= 1.23.0
Requires:         python2-oslo-serialization >= 2.18.0
Requires:         python2-oslo-service >= 1.24.0
Requires:         python2-oslo-utils >= 3.31.0
Requires:         python2-oslo-versionedobjects >= 1.28.0
Requires:         python2-oslo-vmware >= 0.11.1
Requires:         python2-osprofiler >= 1.4.0
Requires:         python-paste
Requires:         python-paste-deploy >= 1.5.0
Requires:         python2-pbr >= 2.0.0
Requires:         python-retrying >= 1.2.3
Requires:         python2-routes >= 2.3.1
Requires:         python-semantic-version >= 2.3.1
Requires:         python2-six >= 1.10.0
Requires:         python2-sqlalchemy >= 1.0.10
Requires:         python2-swiftclient >= 2.2.0
Requires:         python2-taskflow >= 2.7.0
Requires:         python-webob >= 1.7.1
Requires:         python2-wsme >= 0.8.0
Requires:         python2-pyOpenSSL >= 16.2.0

#test deps: python-mox python-nose python-requests
#test and optional store:
#ceph - glance_store.rdb
#python-boto - glance_store.s3
Requires:         python2-boto

Requires(pre):    shadow-utils

%description -n   python-glare
%{common_desc}

This package contains the Glare python library.

%package        common
Summary:        Components common to all OpenStack glare services

Requires:       python-glare = %{version}-%{release}

%description    common
%{common_desc}

%package        api

Summary:        OpenStack Glare api

Requires:       %{name}-common = %{version}-%{release}

%{?systemd_requires}

%description api
%{common_desc}

This package contains the Glare API service.


%package -n python-glare-tests
Summary:        Glare tests
Requires:       python-glare = %{version}-%{release}
Requires:       python2-tempest

%description -n python-glare-tests
%{common_desc}

This package contains the Glare test files.

%if 0%{?with_doc}
%package        doc

Summary:        Documentation for OpenStack Artifact Service

BuildRequires:    python2-sphinx
BuildRequires:    python2-oslo-sphinx
BuildRequires:    python-sphinxcontrib-httpdomain
BuildRequires:    python2-eventlet
BuildRequires:    python2-jsonschema
BuildRequires:    python2-keystoneclient
BuildRequires:    python2-keystonemiddleware
BuildRequires:    python2-oslo-db
BuildRequires:    python2-oslo-log
BuildRequires:    python2-oslo-messaging
BuildRequires:    python2-oslo-policy
BuildRequires:    python2-osprofiler

%description    doc
%{common_desc}

This package contains Openstack Glare documentation
%endif


%prep
%autosetup -n %{service}-%{upstream_version} -S git

find . \( -name .gitignore -o -name .placeholder \) -delete

find glare -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%py_req_cleanup


%build
# Generate config file
PYTHONPATH=. oslo-config-generator --config-file=etc/oslo-config-generator/glare.conf
# Generate oslo policies
PYTHONPATH=. oslopolicy-sample-generator --namespace=glare --output-file=etc/policy.yaml.sample
PYTHONPATH=. sed -i 's/^#"//' etc/policy.yaml.sample
%py2_build

%install
%py2_install

%if 0%{?with_doc}
%{__python2} setup.py build_sphinx -b html
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Install config files
install -p -D -m 644 etc/glare.conf.sample %{buildroot}%{_sysconfdir}/glare/glare.conf
install -p -D -m 644 etc/policy.yaml.sample %{buildroot}%{_sysconfdir}/glare/policy.yaml
install -p -D -m 644 etc/glare-paste.ini %{buildroot}%{_sysconfdir}/glare/glare-paste.ini
install -p -D -m 644 etc/glare-swift.conf.sample %{buildroot}%{_sysconfdir}/glare/glare-swift.conf

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/glare
install -d -m 755 %{buildroot}%{_sharedstatedir}/glare/artifacts
install -d -m 755 %{buildroot}%{_localstatedir}/log/glare

# Install systemd unit services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/%{name}-api.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}-scrubber.service

# Logrotate config
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Remove unused files
rm -f %{buildroot}/usr/etc/glare/*

# Create fake egg-info for the tempest plugin
%py2_entrypoint glare glare

%pre common
getent group glare >/dev/null || groupadd -r glare
if ! getent passwd glare >/dev/null; then
  useradd -r -g glare -G glare -d %{_sharedstatedir}/glare -s /sbin/nologin -c "OpenStack Glare daemon" glare
fi
exit 0

%post api
# Initial installation
%systemd_post %{name}-api.service
%systemd_post %{name}-scrubber.service

%preun api
%systemd_preun %{name}-api.service
%systemd_preun %{name}-scrubber.service

%postun api
%systemd_postun_with_restart %{name}-api.service
%systemd_postun_with_restart %{name}-scrubber.service


%check
%{__python2} setup.py testr


%files -n python-glare
%license LICENSE
%doc README.rst
%{python2_sitelib}/glare
%{python2_sitelib}/glare-*.egg-info
%exclude %{python2_sitelib}/glare/tests
%exclude %{python2_sitelib}/glare_tempest_plugin

%files -n python-glare-tests
%{python2_sitelib}/glare/tests
%{python2_sitelib}/glare_tempest_plugin
%{python2_sitelib}/%{service}_tests.egg-info

%files common
%dir %{_sysconfdir}/glare
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare.conf
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/policy.yaml
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare-paste.ini
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare-swift.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0755, glare, root)  %{_localstatedir}/log/glare

%defattr(-, glare, glare, -)
%dir %{_sharedstatedir}/glare
%dir %{_sharedstatedir}/glare/artifacts

%files api
%{_bindir}/glare-api
%{_bindir}/glare-db-manage
%{_bindir}/glare-scrubber
%{_unitdir}/%{name}-api.service
%{_unitdir}/%{name}-scrubber.service

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%changelog

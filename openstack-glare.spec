%global service glare

%global with_doc 1

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
BuildRequires:    python-pbr
BuildRequires:    python-setuptools
BuildRequires:    openstack-macros
BuildRequires:    systemd
# Required for config generation
BuildRequires:    python-alembic >= 0.8.7
BuildRequires:    python-cryptography >= 1.0
BuildRequires:    python-cursive
BuildRequires:    python-eventlet >= 0.18.2
BuildRequires:    python-futurist >= 0.11.0
BuildRequires:    python-glance-store >= 0.18.0
BuildRequires:    python-httplib2 >= 0.7.5
BuildRequires:    python-iso8601 >= 0.1.11
BuildRequires:    python-jsonpatch >= 1.1
BuildRequires:    python-jsonschema >= 2.0.0
BuildRequires:    python-jwt >= 1.0.1
BuildRequires:    python-keystoneauth1 >= 2.18.0
BuildRequires:    python-keystoneclient >= 1:3.8.0
BuildRequires:    python-keystonemiddleware >= 4.12.0
BuildRequires:    python-memcached >= 1.54
BuildRequires:    python-microversion-parse >= 0.1.2
BuildRequires:    python-monotonic >= 0.6
BuildRequires:    python-os-brick >= 1.8.0
BuildRequires:    python-oslo-concurrency >= 3.8.0
BuildRequires:    python-oslo-config >= 2:3.14.0
BuildRequires:    python-oslo-context >= 2.12.0
BuildRequires:    python-oslo-db-tests
BuildRequires:    python-oslo-i18n >= 2.1.0
BuildRequires:    python-oslo-log >= 3.11.0
BuildRequires:    python-oslo-messaging >= 5.14.0
BuildRequires:    python-oslo-middleware >= 3.0.0
BuildRequires:    python-oslo-policy >= 1.17.0
BuildRequires:    python-oslo-serialization >= 1.10.0
BuildRequires:    python-oslo-service >= 1.10.0
BuildRequires:    python-oslo-utils >= 3.18.0
BuildRequires:    python-oslo-versionedobjects >= 1.17.0
BuildRequires:    python-oslo-vmware >= 0.11.1
BuildRequires:    python-osprofiler >= 1.4.0
BuildRequires:    python-paste
BuildRequires:    python-paste-deploy >= 1.5.0
BuildRequires:    python-pbr >= 1.8
BuildRequires:    python-retrying >= 1.2.3
BuildRequires:    python-routes >= 1.12.3
BuildRequires:    python-semantic-version >= 2.3.1
BuildRequires:    python-six >= 1.9.0
BuildRequires:    python-sqlalchemy >= 1.0.10
BuildRequires:    python-swiftclient >= 2.2.0
BuildRequires:    python-taskflow >= 2.7.0
BuildRequires:    python-webob >= 1.6.0
BuildRequires:    pyOpenSSL >= 0.14
# Required for tests
BuildRequires:    python-os-testr
BuildRequires:    python-oslotest
BuildRequires:    python-testrepository
BuildRequires:    python-testscenarios
BuildRequires:    python-testtools
BuildRequires:    python-mock
BuildRequires:    python-requests-mock

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
Requires:         python-taskflow >= 2.7.0
Requires:         python-webob >= 1.6.0
Requires:         pyOpenSSL >= 0.14

#test deps: python-mox python-nose python-requests
#test and optional store:
#ceph - glance_store.rdb
#python-boto - glance_store.s3
Requires:         python-boto

Requires(pre):    shadow-utils

%description -n   python-glare
OpenStack Glare provides API for catalog of binary data along with its metadata.

This package contains the glare python library.

%package        common
Summary:        Components common to all OpenStack glare services

Requires:       python-glare = %{version}-%{release}

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

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
Requires:       python-tempest

%description -n python-glare-tests
OpenStack Glare provides API for catalog of binary data along with its metadata.

This package contains the Glare test files.

%if 0%{?with_doc}
%package        doc

Summary:        Documentation for OpenStack Artifact Service

BuildRequires:    python-sphinx
BuildRequires:    python-oslo-sphinx
BuildRequires:    python-sphinxcontrib-httpdomain
BuildRequires:    python-eventlet
BuildRequires:    python-jsonschema
BuildRequires:    python-keystoneclient
BuildRequires:    python-keystonemiddleware
BuildRequires:    python-oslo-db
BuildRequires:    python-oslo-log
BuildRequires:    python-oslo-messaging
BuildRequires:    python-oslo-policy
BuildRequires:    python-osprofiler

%description    doc
OpenStack Glare documentaion.
.
This package contains the documentation
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

%post
# Initial installation
%systemd_post %{name}-api.service
%systemd_post %{name}-scrubber.service

%preun
%systemd_preun %{name}-api.service
%systemd_preun %{name}-scrubber.service

%postun
%systemd_postun_with_restart %{name}-api.service
%systemd_postun_with_restart %{name}-scrubber.service


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

%check
%{__python2} setup.py testr

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

# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
%global pyver_entrypoint %py%{pyver}_entrypoint %{service} %{service}
# End of macros for py2/py3 compatibility
%global service glare

# oslosphinx do not work with sphinx > 2
%if %{pyver} == 3
%global with_doc 0
%else
%global with_doc 1
%endif

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
BuildRequires:    python%{pyver}-devel
BuildRequires:    python%{pyver}-pbr
BuildRequires:    python%{pyver}-setuptools
BuildRequires:    openstack-macros
BuildRequires:    systemd
# Required for config generation
BuildRequires:    python%{pyver}-alembic
BuildRequires:    python%{pyver}-cryptography
BuildRequires:    python%{pyver}-cursive
BuildRequires:    python%{pyver}-eventlet
BuildRequires:    python%{pyver}-futurist
BuildRequires:    python%{pyver}-glance-store
BuildRequires:    python%{pyver}-iso8601
BuildRequires:    python%{pyver}-jsonpatch
BuildRequires:    python%{pyver}-jsonschema
BuildRequires:    python%{pyver}-keystoneauth1
BuildRequires:    python%{pyver}-keystoneclient
BuildRequires:    python%{pyver}-keystonemiddleware
BuildRequires:    python%{pyver}-microversion-parse
BuildRequires:    python%{pyver}-os-brick
BuildRequires:    python%{pyver}-oslo-concurrency
BuildRequires:    python%{pyver}-oslo-config
BuildRequires:    python%{pyver}-oslo-context
BuildRequires:    python%{pyver}-oslo-db-tests
BuildRequires:    python%{pyver}-oslo-i18n
BuildRequires:    python%{pyver}-oslo-log
BuildRequires:    python%{pyver}-oslo-messaging
BuildRequires:    python%{pyver}-oslo-middleware
BuildRequires:    python%{pyver}-oslo-policy
BuildRequires:    python%{pyver}-oslo-serialization
BuildRequires:    python%{pyver}-oslo-service
BuildRequires:    python%{pyver}-oslo-utils
BuildRequires:    python%{pyver}-oslo-versionedobjects
BuildRequires:    python%{pyver}-oslo-vmware
BuildRequires:    python%{pyver}-osprofiler
BuildRequires:    python%{pyver}-pbr
BuildRequires:    python%{pyver}-routes
BuildRequires:    python%{pyver}-six
BuildRequires:    python%{pyver}-sqlalchemy
BuildRequires:    python%{pyver}-swiftclient
BuildRequires:    python%{pyver}-taskflow
BuildRequires:    python%{pyver}-webob
BuildRequires:    python%{pyver}-pyOpenSSL
# Required for tests
BuildRequires:    python%{pyver}-stestr
BuildRequires:    python%{pyver}-oslotest
BuildRequires:    python%{pyver}-testrepository
BuildRequires:    python%{pyver}-testscenarios
BuildRequires:    python%{pyver}-testtools
BuildRequires:    python%{pyver}-mock

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:    python-httplib2
BuildRequires:    python-jwt
BuildRequires:    python-memcached
BuildRequires:    python-monotonic
BuildRequires:    python-paste
BuildRequires:    python-paste-deploy
BuildRequires:    python-retrying
BuildRequires:    python-semantic-version
BuildRequires:    python-requests-mock
%else
BuildRequires:    python%{pyver}-httplib2
BuildRequires:    python%{pyver}-jwt
BuildRequires:    python%{pyver}-memcached
BuildRequires:    python%{pyver}-monotonic
BuildRequires:    python%{pyver}-paste
BuildRequires:    python%{pyver}-paste-deploy
BuildRequires:    python%{pyver}-retrying
BuildRequires:    python%{pyver}-semantic_version
BuildRequires:    python%{pyver}-requests-mock
%endif


%description
Glare Artifact Repository


%package -n       python%{pyver}-%{service}
Summary:          OpenStack Glare python libraries
%{?python_provide:%python_provide python%{pyver}-%{service}}


Requires:         python%{pyver}-alembic >= 0.8.10
Requires:         python%{pyver}-cryptography >= 1.9
Requires:         python%{pyver}-eventlet >= 0.18.2
Requires:         python%{pyver}-futurist >= 1.2.0
Requires:         python%{pyver}-glance-store >= 0.22.0
Requires:         python%{pyver}-iso8601 >= 0.1.11
Requires:         python%{pyver}-jsonpatch >= 1.16
Requires:         python%{pyver}-jsonschema >= 2.6.0
Requires:         python%{pyver}-keystoneauth1 >= 3.3.0
Requires:         python%{pyver}-keystoneclient >= 1:3.8.0
Requires:         python%{pyver}-keystonemiddleware >= 4.17.0
Requires:         python%{pyver}-microversion-parse >= 0.1.2
Requires:         python%{pyver}-os-brick >= 1.8.0
Requires:         python%{pyver}-oslo-concurrency >= 3.20.0
Requires:         python%{pyver}-oslo-config >= 2:5.1.0
Requires:         python%{pyver}-oslo-context >= 2.19.2
Requires:         python%{pyver}-oslo-db >= 4.27.0
Requires:         python%{pyver}-oslo-i18n >= 3.15.3
Requires:         python%{pyver}-oslo-log >= 3.30.0
Requires:         python%{pyver}-oslo-messaging >= 5.29.0
Requires:         python%{pyver}-oslo-middleware >= 3.31.0
Requires:         python%{pyver}-oslo-policy >= 1.23.0
Requires:         python%{pyver}-oslo-serialization >= 2.18.0
Requires:         python%{pyver}-oslo-service >= 1.24.0
Requires:         python%{pyver}-oslo-utils >= 3.31.0
Requires:         python%{pyver}-oslo-versionedobjects >= 1.28.0
Requires:         python%{pyver}-oslo-vmware >= 0.11.1
Requires:         python%{pyver}-osprofiler >= 1.4.0
Requires:         python%{pyver}-pbr >= 2.0.0
Requires:         python%{pyver}-routes >= 2.3.1
Requires:         python%{pyver}-six >= 1.10.0
Requires:         python%{pyver}-sqlalchemy >= 1.0.10
Requires:         python%{pyver}-swiftclient >= 2.2.0
Requires:         python%{pyver}-taskflow >= 2.7.0
Requires:         python%{pyver}-webob >= 1.7.1
Requires:         python%{pyver}-wsme >= 0.8.0
Requires:         python%{pyver}-pyOpenSSL >= 16.2.0

# Handle python2 exception
%if %{pyver} == 2
Requires:         python-httplib2 >= 0.9.1
Requires:         python-jwt >= 1.0.1
Requires:         python-memcached >= 1.56
Requires:         python-monotonic >= 0.6
Requires:         python-paste
Requires:         python-paste-deploy >= 1.5.0
Requires:         python-retrying >= 1.2.3
Requires:         python-semantic-version >= 2.3.1
%else
Requires:         python%{pyver}-httplib2 >= 0.9.1
Requires:         python%{pyver}-jwt >= 1.0.1
Requires:         python%{pyver}-memcached >= 1.56
Requires:         python%{pyver}-monotonic >= 0.6
Requires:         python%{pyver}-paste
Requires:         python%{pyver}-paste-deploy >= 1.5.0
Requires:         python%{pyver}-retrying >= 1.2.3
Requires:         python%{pyver}-semantic_version >= 2.3.1
%endif

#test deps: python-mox python-nose python-requests
#test and optional store:
#ceph - glance_store.rdb
#python-boto - glance_store.s3
Requires:         python%{pyver}-boto

Requires(pre):    shadow-utils

%description -n   python%{pyver}-glare
%{common_desc}

This package contains the Glare python library.

%package        common
Summary:        Components common to all OpenStack glare services

Requires:       python%{pyver}-glare = %{version}-%{release}

%description    common
%{common_desc}

%package        api

Summary:        OpenStack Glare api

Requires:       %{name}-common = %{version}-%{release}

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description api
%{common_desc}

This package contains the Glare API service.


%package -n python%{pyver}-glare-tests
Summary:        Glare tests
%{?python_provide:%python_provide python%{pyver}-glare-tests}
Requires:       python%{pyver}-glare = %{version}-%{release}
Requires:       python%{pyver}-tempest

%description -n python%{pyver}-glare-tests
%{common_desc}

This package contains the Glare test files.

%if 0%{?with_doc}
%package        doc

Summary:        Documentation for OpenStack Artifact Service

BuildRequires:    python%{pyver}-sphinx
BuildRequires:    python%{pyver}-oslo-sphinx
BuildRequires:    python%{pyver}-eventlet
BuildRequires:    python%{pyver}-jsonschema
BuildRequires:    python%{pyver}-keystoneclient
BuildRequires:    python%{pyver}-keystonemiddleware
BuildRequires:    python%{pyver}-oslo-db
BuildRequires:    python%{pyver}-oslo-log
BuildRequires:    python%{pyver}-oslo-messaging
BuildRequires:    python%{pyver}-oslo-policy
BuildRequires:    python%{pyver}-osprofiler
# Handle python2 exception
%if %{pyver} == 2
BuildRequires:    python-sphinxcontrib-httpdomain
%else
BuildRequires:    python%{pyver}-sphinxcontrib-httpdomain
%endif

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
PYTHONPATH=. oslo-config-generator-%{pyver} --config-file=etc/oslo-config-generator/glare.conf
# Generate oslo policies
PYTHONPATH=. oslopolicy-sample-generator-%{pyver} --namespace=glare --output-file=etc/policy.yaml.sample
PYTHONPATH=. sed -i 's/^#"//' etc/policy.yaml.sample
%{pyver_build}

%install
%{pyver_install}

%if 0%{?with_doc}
%{pyver_bin} setup.py build_sphinx -b html
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
%pyver_entrypoint

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
PYTHON=%{pyver_bin} stestr-%{pyver} run --black-regex 'glare.tests.unit.test_unpacking.TestArtifactHooks.test_unpacking_database_big_archive|glare.tests.unit.test_unpacking.TestArtifactHooks.test_unpacking_big_archive'


%files -n python%{pyver}-glare
%license LICENSE
%doc README.rst
%{pyver_sitelib}/glare
%{pyver_sitelib}/glare-*.egg-info
%exclude %{pyver_sitelib}/glare/tests
%exclude %{pyver_sitelib}/glare_tempest_plugin

%files -n python%{pyver}-glare-tests
%{pyver_sitelib}/glare/tests
%{pyver_sitelib}/glare_tempest_plugin
%{pyver_sitelib}/%{service}_tests.egg-info

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

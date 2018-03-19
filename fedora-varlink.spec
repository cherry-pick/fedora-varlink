Name:           fedora-varlink
Version:        3
Release:        1%{?dist}
Summary:        Fedora Varlink System Interfaces
License:        ASL2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  systemd
Requires:       org.kernel.kmod
Requires:       org.varlink.http
Requires:       com.redhat.resolver
Requires:       com.redhat.accounts
Requires:       com.redhat.devices
Requires:       com.redhat.logging
Requires:       com.redhat.machine
Requires:       com.redhat.network
Requires:       libvarlink-util

%description
Fedora Varlink System Interface configuration.

%prep
%setup -q

%install
install -d %{buildroot}%{_prefix}/lib
install fedora.json %{buildroot}%{_prefix}/lib
sed -i -e 's#"version":\s*"[0-9]\+"#"version": "%{fedora}"#' %{buildroot}%{_prefix}/lib/fedora.json

install -d %{buildroot}%{_unitdir}
install -m 0644 com.redhat.resolver.service %{buildroot}%{_unitdir}
install -m 0644 org.varlink.resolver.socket %{buildroot}%{_unitdir}

%post
%systemd_post com.redhat.resolver.service org.varlink.resolver.socket

%preun
%systemd_preun com.redhat.resolver.service org.varlink.resolver.socket

%postun
%systemd_postun

%files
%{_prefix}/lib/fedora.json
%{_unitdir}/com.redhat.resolver.service
%{_unitdir}/org.varlink.resolver.socket

%changelog
* Mon Mar 19 2018 <info@varlink.org> 3-1
- fedora-varlink 3

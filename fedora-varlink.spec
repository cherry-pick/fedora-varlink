Name:           fedora-varlink
Version:        1
Release:        1%{?dist}
Summary:        Fedora Varlink System Interfaces
License:        ASL2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  systemd
Requires:       io.systemd.devices
Requires:       io.systemd.journal
Requires:       io.systemd.network
Requires:       io.systemd.sysinfo
Requires:       org.kernel.kmod
Requires:       org.varlink.http
Requires:       org.varlink.resolver
Requires:       com.redhat.system

%description
Fedora Varlink System Interface configuration.

%prep
%setup -q

%install
install -d %{buildroot}%{_prefix}/lib
install fedora.json %{buildroot}%{_prefix}/lib

install -d %{buildroot}%{_unitdir}
install -m 0644 org.varlink.resolver.service %{buildroot}%{_unitdir}
install -m 0644 org.varlink.resolver.socket %{buildroot}%{_unitdir}

%post
%systemd_post org.varlink.resolver.service org.varlink.resolver.socket

%preun
%systemd_preun org.varlink.resolver.service org.varlink.resolver.socket

%postun
%systemd_postun

%files
%{_prefix}/lib/fedora.json
%{_unitdir}/org.varlink.resolver.service
%{_unitdir}/org.varlink.resolver.socket

%changelog
* Tue Aug 29 2017 <info@varlink.org> 1-1
- fedora-varlink 1

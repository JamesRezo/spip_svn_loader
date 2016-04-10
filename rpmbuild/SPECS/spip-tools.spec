%define debug_package %{nil}

Name:           spip-tools
Version:        1.0.0
Release:        beta6%{?dist}
Summary:        Outils pour SPIP

License:        MIT
URL:            https://github.com/JamesRezo/spip_svn_loader
BuildArch:      noarch
Source0:        spip-tools-1.0.0.tar.gz

Requires:       bash subversion php-cli php-xml curl findutils

%description
Installer et mettre a jour SPIP avec SVN

%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/opt/spip-tools/bin
install -m 755 opt/spip-tools/bin/spip_svn_loader ${RPM_BUILD_ROOT}/opt/spip-tools/bin

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
ln -s -f /opt/spip-tools/bin/spip_svn_loader /usr/local/bin/spip_svn_loader

%postun
%{__rm} -f /usr/local/bin/spip_svn_loader

%files
%defattr(-,root,root)
%attr(755,root,root) /opt/spip-tools/bin/spip_svn_loader


%changelog
* Sun Apr  3 2016 JamesRezo
- Installation
 

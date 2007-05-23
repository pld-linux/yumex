Summary:	YumExtender - a graphical frontend to yum
Name:		yumex
Version:	1.9.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.yum-extender.org/dnl/yumex/source/%{name}-%{version}.tar.gz
# Source0-md5:	d48a858c5dfb307c724a2c2c2bcc4e00
Patch0:		%{name}-yum-config.patch
Patch1:		%{name}-gnomesu.patch
URL:		http://www.yum-extender.org/
BuildRequires:	gettext-devel
Requires:	gnomesu
Requires:	yum
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YumExtender - a graphical frontend to yum

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYLIBDIR=%{py_sitescriptdir}/..

rm $RPM_BUILD_ROOT%{_bindir}/yumex
ln -s /usr/share/yumex/yumex $RPM_BUILD_ROOT%{_bindir}/yumex

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yumex.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yumex.profiles.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pam.d/yumex
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/security/console.apps/yumex
%attr(755,root,root) %{_bindir}/yumex
%dir %{py_sitescriptdir}/yumgui
%{py_sitescriptdir}/*/*.py[co]
%{_desktopdir}/yumex.desktop
%dir %{_datadir}/yumex
%attr(755,root,root) %{_datadir}/yumex/yumex
%{_datadir}/yumex/*.py*
%{_datadir}/yumex/*.glade
%{_pixmapsdir}/yumex

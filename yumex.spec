Summary:	YumExtender - a graphical frontend to yum
Summary(pl.UTF-8):	YumExtender - graficzny interfejs dla yuma
Name:		yumex
Version:	2.0.5
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.yum-extender.org/dnl/yumex/source/%{name}-%{version}.tar.gz
# Source0-md5:	57686187efb6abe645b416f4b63d9c37
Source1:	%{name}-gtk.desktop
Source2:	%{name}-kde.desktop
Patch0:		%{name}-yum-config.patch
Patch1:		%{name}-missingok.patch
Patch2:		%{name}-obsoletes.patch
URL:		http://www.yum-extender.org/
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python-pygtk-glade
Requires:	yum
Suggests:	gksu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YumExtender - a graphical frontend to yum.

%description -l pl.UTF-8
YumExtender - graficzny interfejs dla yuma.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

cat << 'EOF' > misc/yumex
#!/bin/sh
#
# Run yumex main python program.
#
exec %{__python} %{_datadir}/yumex/yumex.pyc ${1:+"$@"}
EOF

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYLIBDIR=%{py_sitescriptdir}/..

mv -f $RPM_BUILD_ROOT{%{_datadir}/yumex,%{_bindir}}/yumex
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/yumex.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/yumex-kde.desktop

rm -f $RPM_BUILD_ROOT%{_datadir}/yumex/COPYING
%py_postclean %{_datadir}/yumex

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yumex.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yumex.profiles.conf
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/yumex
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.apps/yumex
%attr(755,root,root) %{_bindir}/yumex
%dir %{py_sitescriptdir}/yumgui
%{py_sitescriptdir}/*/*.py[co]
%{_desktopdir}/*.desktop
%dir %{_datadir}/yumex
%{_datadir}/yumex/*.py[co]
%{_datadir}/yumex/*.glade
%{_pixmapsdir}/yumex

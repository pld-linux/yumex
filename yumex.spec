Summary:	YumExtender - a graphical frontend to yum
Summary(pl.UTF-8):	YumExtender - graficzny interfejs dla yuma
Name:		yumex
Version:	1.9.9
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.yum-extender.org/dnl/yumex/source/%{name}-%{version}.tar.gz
# Source0-md5:	9c3b785819940eaf25e449a8c466478b
Source1:	%{name}-gtk.desktop
Source2:	%{name}-kde.desktop
Patch0:		%{name}-yum-config.patch
#Patch1:		%{name}-pl.patch
#Patch2:		%{name}-glade.patch
#Patch3:		%{name}-icons.patch
#Patch4:		%{name}-glade2.patch
Patch5:		%{name}-missingok.patch
Patch6:		%{name}-obsoletes.patch
URL:		http://www.yum-extender.org/
BuildRequires:	gettext-devel
Requires:	gksu
Requires:	python-pygtk-glade
Requires:	yum
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YumExtender - a graphical frontend to yum.

%description -l pl.UTF-8
YumExtender - graficzny interfejs dla yuma.

%prep
%setup -q
%patch0 -p1
#%%patch1 -p1
#%%patch2 -p1
#%%patch3 -p1
#%%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYLIBDIR=%{py_sitescriptdir}/..

rm $RPM_BUILD_ROOT%{_bindir}/yumex
ln -s %{_datadir}/yumex/yumex $RPM_BUILD_ROOT%{_bindir}/yumex
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/yumex.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/yumex-kde.desktop

rm -f $RPM_BUILD_ROOT%{_datadir}/yumex/COPYING
%py_postclean

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
%attr(755,root,root) %{_datadir}/yumex/yumex
%{_datadir}/yumex/*.py*
%{_datadir}/yumex/*.glade
%{_pixmapsdir}/yumex

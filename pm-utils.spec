Summary:	Power management utilities and scripts
Summary(pl.UTF-8):	Narzędzia i skrypty do zarządzania energią
Name:		pm-utils
Version:	0.99.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://cvs.fedoraproject.org/repo/pkgs/pm-utils/pm-utils-0.99.4.tar.gz/a88503876f63c96b55784be91b6458d2/%{name}-%{version}.tar.gz
# Source0-md5:	a88503876f63c96b55784be91b6458d2
Patch0:		%{name}-cfg.patch
Patch1:		%{name}-uswsusp-support.patch
URL:		http://pm-utils.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pm-utils package contains utilities and scripts useful for tasks
related to power management.

%description -l pl.UTF-8
Pakiet pm-utils zawiera narzędzia i skrypty pomocne przy zadaniach
związanych z zarządzaniem energią.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/log

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_var}/log/pm-suspend.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/pm
%dir %{_sysconfdir}/pm/config.d
%dir %{_sysconfdir}/pm/power.d
%dir %{_sysconfdir}/pm/sleep.d
%attr(755,root,root) %{_bindir}/on_ac_power
%attr(755,root,root) %{_bindir}/pm-is-supported
%dir %{_libdir}/pm-utils
%dir %{_libdir}/pm-utils/bin
%attr(755,root,root) %{_libdir}/pm-utils/bin/pm-action
%attr(755,root,root) %{_libdir}/pm-utils/bin/pm-pmu
%attr(755,root,root) %{_libdir}/pm-utils/bin/pm-reset-swap
%dir %{_libdir}/pm-utils/power.d
%attr(755,root,root) %{_libdir}/pm-utils/power.d/sched-powersave
%dir %{_libdir}/pm-utils/sleep.d
%attr(755,root,root) %{_libdir}/pm-utils/sleep.d/*
%{_libdir}/pm-utils/defaults
%{_libdir}/pm-utils/functions
%attr(755,root,root) %{_sbindir}/pm-hibernate
%attr(755,root,root) %{_sbindir}/pm-powersave
%attr(755,root,root) %{_sbindir}/pm-suspend
%attr(755,root,root) %{_sbindir}/pm-suspend-hybrid
%{_mandir}/man1/*.1*
%ghost %{_var}/log/pm-suspend.log

Summary:	Power management utilities and scripts
Summary(pl.UTF-8):	Narzędzia i skrypty do zarządzania energią
Name:		pm-utils
Version:	1.1.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://pm-utils.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a9fcb1ee69ddc24bcc174ebf56f2cf11
URL:		http://pm-utils.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
Requires:	hal
%ifarch %{ix86} %{x8664}
Requires:	vbetool
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pm-utils package contains utilities and scripts useful for tasks
related to power management.

%description -l pl.UTF-8
Pakiet pm-utils zawiera narzędzia i skrypty pomocne przy zadaniach
związanych z zarządzaniem energią.

%prep
%setup -q

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
%dir %{_libdir}/pm-utils/module.d
%attr(755,root,root) %{_libdir}/pm-utils/module.d/kernel
%attr(755,root,root) %{_libdir}/pm-utils/module.d/tuxonice
%attr(755,root,root) %{_libdir}/pm-utils/module.d/uswsusp
%dir %{_libdir}/pm-utils/power.d
%attr(755,root,root) %{_libdir}/pm-utils/power.d/sched-powersave
%dir %{_libdir}/pm-utils/sleep.d
%attr(755,root,root) %{_libdir}/pm-utils/sleep.d/*
%{_libdir}/pm-utils/defaults
%{_libdir}/pm-utils/functions
%{_libdir}/pm-utils/pm-functions
%attr(755,root,root) %{_sbindir}/pm-hibernate
%attr(755,root,root) %{_sbindir}/pm-powersave
%attr(755,root,root) %{_sbindir}/pm-suspend
%attr(755,root,root) %{_sbindir}/pm-suspend-hybrid
%{_mandir}/man1/*.1*
%{_pkgconfigdir}/pm-utils.pc
%ghost %{_var}/log/pm-suspend.log

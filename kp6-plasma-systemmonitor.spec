#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.2.3
%define		qtver		5.15.2
%define		kpname		plasma-systemmonitor
%define		kf6ver		5.39.0

Summary:	plasma-systemmonitor
Name:		kp6-%{kpname}
Version:	6.2.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	cbbcd79945028a2e39e7ebcd91b694c2
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= 5.15.0
BuildRequires:	Qt6Gui-devel >= 5.15.0
BuildRequires:	Qt6Network-devel >= 5.15.0
BuildRequires:	Qt6Qml-devel >= 5.15.2
BuildRequires:	Qt6Quick-devel >= 5.15.0
BuildRequires:	Qt6Widgets-devel >= 5.15.0
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.82
BuildRequires:	kf6-kconfig-devel >= 5.82
BuildRequires:	kf6-kdbusaddons-devel >= 5.82
BuildRequires:	kf6-kdeclarative-devel >= 5.82
BuildRequires:	kf6-kglobalaccel-devel >= 5.82
BuildRequires:	kf6-ki18n-devel >= 5.82
BuildRequires:	kf6-kiconthemes-devel >= 5.82
BuildRequires:	kf6-kio-devel >= 5.82
BuildRequires:	kf6-kitemmodels-devel >= 5.82
BuildRequires:	kf6-knewstuff-devel >= 5.82
BuildRequires:	kf6-kservice-devel >= 5.85.0
BuildRequires:	kp6-libksysguard-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
An application for monitoring system resources.

plasma-systemmonitor provides an interface for monitoring system
sensors, process information and other system resources. It is built
on top of the faces system also used to provide widgets for
plasma-dekstop and makes use of the ksystemstats daemon to provide
sensor information. It allows extensive customisation of pages, so it
can be made to show exactly which data people want to see.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-systemmonitor
%attr(755,root,root) %{_libdir}/libPlasmaSystemMonitorPage.so
%attr(755,root,root) %{_libdir}/libPlasmaSystemMonitorTable.so
%{_datadir}/kglobalaccel/org.kde.plasma-systemmonitor.desktop
%{_libdir}/qt6/qml/org/kde/ksysguard/page
%{_libdir}/qt6/qml/org/kde/ksysguard/table
%{_desktopdir}/org.kde.plasma-systemmonitor.desktop
%{_datadir}/config.kcfg/systemmonitor.kcfg
%{_datadir}/knsrcfiles/plasma-systemmonitor.knsrc
%{_datadir}/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable
%{_datadir}/ksysguard/sensorfaces/org.kde.ksysguard.processtable
%{_datadir}/plasma-systemmonitor
%dir %{_datadir}/plasma/kinfocenter
%dir %{_datadir}/plasma/kinfocenter/externalmodules
%{_datadir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%{_datadir}/metainfo/org.kde.plasma-systemmonitor.metainfo.xml

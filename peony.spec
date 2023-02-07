Name:          peony
Version:       3.10.0
Release:       2
Summary:       file Manager for the UKUI desktop
License:       GPL-3.0-or-later and MIT and BSD-3-Clause
URL:           http://www.ukui.org
Source0:       %{name}-%{version}.tar.gz

BuildRequires: libudisks2-devel
BuildRequires: libnotify-devel
BuildRequires: gtk2-devel
BuildRequires: pkg-config, qt5-qtbase-devel, qt5-qtbase-private-devel, qtchooser, glib2-devel, qt5-qtx11extras-devel, gsettings-qt-devel, poppler-devel, poppler-qt5-devel, kf5-kwindowsystem-devel, libcanberra-devel
BuildRequires: openssl-devel
BuildRequires: kf5-kwayland
BuildRequires: kf5-kwayland-devel
BuildRequires: wayland-devel
BuildRequires: qt5-qttools-devel
BuildRequires: ukui-interface
BuildRequires: bamf-devel qt5-qtsvg-devel qt5-qtdeclarative-devel

Requires: peony-common, libpeony3
Requires: qt5-qttranslations
Requires: gvfs, dvd+rw-tools ,libcanberra-devel


%description
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.

%package common
Summary:     file manager for the UKUI desktop (common files)
License:     GPL-3.0-or-later
BuildRequires: pkg-config, qt5-qtbase-devel, qt5-qtbase-private-devel, qtchooser, glib2-devel, qt5-qtx11extras-devel, gsettings-qt-devel, poppler-devel, poppler-qt5-devel, kf5-kwindowsystem-devel


%description common
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains the architecture independent files.

%package -n libpeony3
Summary:     libraries for Peony components
License:     LGPL-3.0-or-later and MIT and BSD-3-Clause
BuildRequires: pkg-config, qt5-qtbase-devel, qt5-qtbase-private-devel, qtchooser, glib2-devel, qt5-qtx11extras-devel, gsettings-qt-devel, poppler-devel, poppler-qt5-devel, kf5-kwindowsystem-devel
Provides: libpeony

%description -n libpeony3
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains a few runtime libraries needed by Peony's
 extensions

%package -n libpeony-dev
Summary:     libraries for Peony components (development files)
License:     LGPL-3.0-or-later and MIT and BSD-3-Clause
#BuildRequires: pkg-config, qt5-qtbase-devel, qt5-qtbase-private-devel, qtchooser, glib2-devel, qt5-qtx11extras-devel,
# gsettings-qt-devel, poppler-devel, poppler-qt5-devel, kf5-kwindowsystem-devel
Provides: libpeony

%description -n libpeony-dev
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains the development files for the libraries needed
 by Peony's extensions.


%prep
%setup -q

%build
%{qmake_qt5}
%{make_build}


%install
rm -rf $RPM_BUILD_ROOT
%{make_install} INSTALL_ROOT=%{buildroot}

#peony-common
mkdir -p %{buildroot}/usr/share/dbus-1/interfaces
mkdir -p %{buildroot}/usr/share/dbus-1/services
mkdir -p %{buildroot}/usr/share/peony-qt
mkdir -p %{buildroot}/usr/share/peony-qt-desktop
mkdir -p %{buildroot}/usr/share/kylin-user-guide/data/guide/peony

cp -r %{_builddir}/%{name}-%{version}/peony-qt-desktop/freedesktop-dbus-interfaces.xml %{buildroot}/usr/share/dbus-1/interfaces
cp -r %{_builddir}/%{name}-%{version}/peony-qt-desktop/org.ukui.freedesktop.FileManager1.service %{buildroot}/usr/share/dbus-1/services
cp -r %{_builddir}/%{name}-%{version}/translations/peony-qt/* %{buildroot}/usr/share/peony-qt
cp -r %{_builddir}/%{name}-%{version}/translations/peony-qt-desktop/* %{buildroot}/usr/share/peony-qt-desktop
cp -r %{_builddir}/%{name}-%{version}/data/peony/* %{buildroot}/usr/share/kylin-user-guide/data/guide/peony/

#libpeony3
mkdir -p %{buildroot}/usr/share/libpeony-qt
cp -r %{_builddir}/%{name}-%{version}/translations/libpeony-qt/* %{buildroot}/usr/share/libpeony-qt

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_prefix}/bin/*
%{_datadir}/applications/*

%files common
%doc debian/copyright debian/changelog
%{_datadir}/dbus-1/interfaces/*
%{_datadir}/dbus-1/services/*
%{_datadir}/glib-2.0/schemas/org.ukui.peony.settings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.peony.desktop.settings.gschema.xml
%{_datadir}/peony-qt/*
%{_datadir}/peony-qt-desktop/*
%{_datadir}/kylin-user-guide/data/guide/peony
%{_sysconfdir}/xdg/autostart/peony-desktop.desktop


%files -n libpeony3
%{_prefix}/%{_lib}/*.so.*
%{_datadir}/libpeony-qt/*

%files -n libpeony-dev
%{_prefix}/include/peony-qt/*
%{_prefix}/%{_lib}/pkgconfig/*.pc
%{_prefix}/%{_lib}/*.so

%changelog
* Tue Feb 07 2023 peijiankang <peijiankang@kylinos.cn> - 3.10.0-2
- add build debuginfo and debugsource

* Mon Nov 14 2022 tanyulong <tanyulong@kylinos.cn> - 3.10.0-1
- update version 3.10.0

* Wed Jul 13 2022 peijiankang <peijiankang@kylinos.cn> - 3.2.4-4
- add qt5-qttranslations

* Thu Jun 9 2022 peijiankang <peijiankang@kylinos.cn> - 3.2.4-3
- add kylin-user-guide files 

* Wed Apr 27 2022 wangyueliang <wangyueliang@kylinos.cn> - 3.2.4-2
- Improve the project according to the requirements of compliance improvement.

* Tue Feb 22 2022 tanyulong <tanyulong@kylinos.cn> - 3.2.4-1
- update version 3.2.4

* Tue Oct 26 2021 douyan <douyan@kylinos.cn> - 3.0.4-2
- add patch:0001-adjust-desktop-readonly-icon-agree-with-icon-view.patch

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.4-1
- update to upstream version 3.0.4

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.1.2-1
- Init package for openEuler

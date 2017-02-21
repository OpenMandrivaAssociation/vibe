%define major 0
%define libvibecore %mklibname VibeCore %{major}
%define libvibesettings %mklibname VibeSettings %{major}
%define devname %mklibname -d VibeCore

Summary:        A collection of core classes used throughout Liri
Name:           vibe
Version:        0.9.0
Release:        1
License:	LGPLv3
Url:		https://github.com/lirios/
Source0:	https://github.com/lirios/vibe/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	cmake(Fluid)
BuildRequires:	qt5-devel
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickTest)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(PolkitQt5-1)
BuildRequires:	cmake(ECM)

%description
A collection of core classes used throughout Liri.

%package -n     %{libvibecore}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libvibecore}
Library for %{name}

%package -n     %{libvibesettings}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libvibecore}
Library for %{name}.

%package -n     %{devname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libvibecore} = %{EVRD}
Requires:       %{libvibesettings} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{devname}
Components for Qt Quick applications with Material Design and Universal
development files.

%prep
%setup -q
%cmake_qt5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_bindir}/liri-notify
%{_libdir}/qml/Vibe

%files -n %{libvibecore}
%{_libdir}/libVibeCore.so.%{major}*

%files -n %{libvibesettings}
%{_libdir}/libVibeSettings.so.%{major}*

%files -n %{devname}
%{_libdir}/libVibeCore.so
%{_libdir}/libVibeSettings.so
%{_includedir}/Vibe/
%{_libdir}/cmake/Vibe/

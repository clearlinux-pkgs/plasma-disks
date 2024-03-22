#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 61973a3
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-disks
Version  : 6.0.2
Release  : 3
URL      : https://download.kde.org/stable/plasma/6.0.2/plasma-disks-6.0.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.2/plasma-disks-6.0.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.2/plasma-disks-6.0.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 FSFAP GPL-2.0 GPL-3.0 LGPL-3.0
Requires: plasma-disks-data = %{version}-%{release}
Requires: plasma-disks-lib = %{version}-%{release}
Requires: plasma-disks-license = %{version}-%{release}
Requires: plasma-disks-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : kservice-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the plasma-disks package.
Group: Data

%description data
data components for the plasma-disks package.


%package lib
Summary: lib components for the plasma-disks package.
Group: Libraries
Requires: plasma-disks-data = %{version}-%{release}
Requires: plasma-disks-license = %{version}-%{release}

%description lib
lib components for the plasma-disks package.


%package license
Summary: license components for the plasma-disks package.
Group: Default

%description license
license components for the plasma-disks package.


%package locales
Summary: locales components for the plasma-disks package.
Group: Default

%description locales
locales components for the plasma-disks package.


%prep
%setup -q -n plasma-disks-6.0.2
cd %{_builddir}/plasma-disks-6.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710795979
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710795979
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-disks
cp %{_builddir}/plasma-disks-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-disks/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-disks/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/FSFAP.txt %{buildroot}/usr/share/package-licenses/plasma-disks/e91dcdf6eb4e675db1aee8b8fb8394bdfcb22d49 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-disks/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-disks/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-disks/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-disks/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-disks/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-disks/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-disks-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-disks/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/broken.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/cli.txt.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/error-info-log-failed.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/fail.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/failing-sectors-passing-status.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/invalid-cmdline-bad-usb-bridge.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/invalid-vbox.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/missing-status.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/pass-freebsd.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/pass-without-status.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/plasma-disks-%{version}/autotests/fixtures/pass.json.license %{buildroot}/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcm_disks

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf6/kauth/kded-smart-helper

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_disks.desktop
/usr/share/dbus-1/system-services/org.kde.kded.smart.service
/usr/share/dbus-1/system.d/org.kde.kded.smart.conf
/usr/share/knotifications6/org.kde.kded.smart.notifyrc
/usr/share/metainfo/org.kde.plasma.disks.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/kf6/kded/smart.so
/usr/lib64/qt6/plugins/plasma/kcms/kinfocenter/kcm_disks.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-disks/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/plasma-disks/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/plasma-disks/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/plasma-disks/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-disks/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/plasma-disks/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/plasma-disks/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-disks/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/plasma-disks/e91dcdf6eb4e675db1aee8b8fb8394bdfcb22d49

%files locales -f kcm_disks.lang
%defattr(-,root,root,-)


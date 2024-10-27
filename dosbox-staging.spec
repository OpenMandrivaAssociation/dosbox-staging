Name: dosbox-staging
Version: 0.82.0
Release: 1
Source0: https://github.com/dosbox-staging/dosbox-staging/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Summary: DOS Emulator
URL: https://github.com/dosbox-staging/dosbox-staging
License: GPLv2+
Group: Emulators
BuildRequires: meson ninja
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_net)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(slirp) >= 4.6.1
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(mt32emu)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(iir)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: atomic-devel
Obsoletes: dosbox < %{EVRD}

%description
DOSBox is a DOS emulator, emulating 286/386 CPUs, filesystems,
XMS/EMS, various graphics cards and sound cards.

DOSBox-staging is a fork of DOSBox that tries to modernize the codebase
and add new features.

%prep
%autosetup -p1
%meson

%build
%ninja_build -C build

%install
%ninja_install -C build

%check
%ninja_build -C build test

%files
%doc %{_docdir}/%{name}
%license %{_datadir}/licenses/dosbox-staging/
%{_bindir}/dosbox
#{_datadir}/applications/dosbox-staging.desktop
%dir %{_datadir}/dosbox-staging
#{_datadir}/icons/*/*/apps/dosbox-staging.*
#{_datadir}/metainfo/dosbox-staging.metainfo.xml
%{_mandir}/man1/dosbox.1*
%{_datadir}/dosbox-staging/drives/y.conf
%{_datadir}/dosbox-staging/drives/y
%{_datadir}/dosbox-staging/freedos-cpi
%{_datadir}/dosbox-staging/freedos-keyboard
%{_datadir}/dosbox-staging/glshaders
%{_datadir}/dosbox-staging/mapperfiles
%{_datadir}/dosbox-staging/mapping-freedos.org
%{_datadir}/dosbox-staging/mapping-unicode.org
%{_datadir}/dosbox-staging/mapping-wikipedia.org
%{_datadir}/dosbox-staging/mapping
%dir %{_datadir}/dosbox-staging/translations
%lang(br) %{_datadir}/dosbox-staging/translations/br.lng
%lang(de) %{_datadir}/dosbox-staging/translations/de.lng
%lang(en) %{_datadir}/dosbox-staging/translations/en.lng
%lang(es) %{_datadir}/dosbox-staging/translations/es.lng
%lang(fr) %{_datadir}/dosbox-staging/translations/fr.lng
%lang(it) %{_datadir}/dosbox-staging/translations/it.lng
%lang(nl) %{_datadir}/dosbox-staging/translations/nl.lng
%lang(pl) %{_datadir}/dosbox-staging/translations/pl.lng
%lang(ru) %{_datadir}/dosbox-staging/translations/ru.lng

Summary:	Real-time MIDI sequencer
Summary(pl):	Sekwencer MIDI dzia³aj±cy w czasie rzeczywistym
Name:		seq24
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://filter24.org/seq24/%{name}-%{version}.tar.gz
# Source0-md5:	bea461bf65ba6ddcb57ce62f20cbcd34
Source1:	%{name}.desktop
URL:		http://filter24.org/seq24/
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm1-devel >= 1.2.9
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seq24 is a real-time midi sequencer. It was created to provide a very
simple interface for editing and playing MIDI 'loops'.

%description -l pl
Seq24 jest sekwencerem dzia³aj±cym w czasie rzeczywistym. Zosta³
stworzony z my¶l± o prostocie interfejsu do edycji i odtwarzania
'pêtli' MIDI.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README RTC SEQ24
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop

Summary:	Noto Emoji fonts
Name:		fonts-TTF-Google-noto-emoji
Version:	2.034
Release:	1
License:	OFL v1.1
Group:		Fonts
URL:		https://github.com/googlefonts/noto-emoji
Source0:	https://github.com/googlefonts/noto-emoji/archive/v%{version}/noto-emoji-%{version}.tar.gz
# Source0-md5:	6fc89f4ffbf8c9be68e94f5d99d02090
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Color and Black-and-White Noto emoji fonts.

%prep
%setup -q -n noto-emoji-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ttffontsdir}
cp -p fonts/{NotoColorEmoji,NotoEmoji-Regular}.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc fonts/LICENSE
%{_ttffontsdir}/NotoEmoji-Regular.ttf
%{_ttffontsdir}/NotoColorEmoji.ttf

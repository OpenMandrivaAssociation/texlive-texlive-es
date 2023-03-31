Name:		texlive-texlive-es
Version:	62677
Release:	2
Summary:	TeX Live manual (Spanish)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlive-es
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-es.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-es.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/texlive/texlive-es

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

# revision 24793
# category Package
# catalog-ctan /macros/latex/contrib/sasnrdisplay
# catalog-date 2011-12-02 09:08:13 +0100
# catalog-license lppl1.3
# catalog-version 0.9
Name:		texlive-sasnrdisplay
Version:	0.9
Release:	1
Summary:	Typeset SAS or R code or output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sasnrdisplay
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sasnrdisplay.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sasnrdisplay.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The SASnRdisplay package serves as a front-end to the listings,
which permits statisticians and others to import source code,
and the results of their calculations or simulations into LaTeX
projects. The package is also capable of overloading the Sweave
and SASweave packages.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sasnrdisplay/SASnRdisplay.cfg
%{_texmfdistdir}/tex/latex/sasnrdisplay/SASnRdisplay.sty
%doc %{_texmfdistdir}/doc/latex/sasnrdisplay/README
%doc %{_texmfdistdir}/doc/latex/sasnrdisplay/SASnRdisplay.pdf
%doc %{_texmfdistdir}/doc/latex/sasnrdisplay/SASnRdisplay.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

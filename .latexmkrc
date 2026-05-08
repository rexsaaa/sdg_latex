my $tex_file = '';

foreach my $arg (@ARGV) {
    next if $arg =~ /^-/;
    if ($arg =~ /\.tex$/) {
        $tex_file = $arg;
        last;
    }
}

$tex_file =~ s{\\}{/}g;

if ($tex_file =~ m{(^|/)manuscripts/compare/} || $tex_file =~ m{(^|/)main_compare\.tex$}) {
    $out_dir = 'build/compare';
    $aux_dir = 'build/compare';
} elsif ($tex_file =~ m{(^|/)manuscripts/trans/} || $tex_file =~ m{(^|/)main_trans\.tex$}) {
    $out_dir = 'build/trans';
    $aux_dir = 'build/trans';
} elsif ($tex_file =~ m{(^|/)manuscripts/zh/} || $tex_file =~ m{(^|/)main_zh\.tex$} || $tex_file =~ m{(^|/)main\.tex$}) {
    $out_dir = 'build/zh';
    $aux_dir = 'build/zh';
} else {
    $out_dir = 'build';
    $aux_dir = 'build';
}

Baseline emissions 261.4 Mt; Lambda 1.5947 Mt per $/t (0.610% per $/t)
Gamma (second derivative of uniform-tax cut) -0.04172
Power: emission share 0.455; weight switching 0.551, demand 0.122; kappa 0.00815 t/$; X 14600 $m; omega_int_s 0.819
Road transport: emission share 0.308; weight switching 0.008, demand 0.047; kappa 0.00232 t/$; X 34720 $m; omega_int_s 0.143
Industry: emission share 0.237; weight switching 0.181, demand 0.092; kappa 0.00785 t/$; X 7900 $m; omega_int_s 0.664
Economy: switching share of Lambda 0.740
LCFS credit price 166.0 $/t; renewable output with subsidy 51.4 TWh; subsidy spending 514 $m; budgetary cost per tonne 78.5 $/t
Covered-emissions-weighted shadow price of the standard 51.1 $/t

| Instrument | TECP switching | TECP demand | TECP first order | TECP second order | TECP exact | cut exact Mt | cut linear | cut 2nd | explicit | explicit+shadow |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| tax | 21.97 | 6.40 | 28.36 | 27.21 | 27.23 | 32.57 | 45.23 | 26.61 | 20.8 | 20.8 |
| subsidy | 4.09 | -0.41 | 3.68 | 4.24 | 4.34 | 6.55 | 5.87 | 6.48 | 0.0 | 0.0 |
| standard | 1.01 | 0.16 | 1.16 | 1.17 | 1.17 | 1.84 | 1.85 | 1.84 | 0.0 | 51.1 |
| mix | 27.06 | 6.14 | 33.21 | 36.23 | 36.86 | 40.72 | 52.95 | 34.78 | 20.8 | 71.8 |
Sum of stand-alone exact TECPs 32.74; sum of stand-alone exact cuts 40.96
Old (1 - w) form TECP of the mix: 31.66

Accuracy, mix scaled by k: k, linear, second, exact, err lin %, err 2nd %
  0.5: 16.60, 17.36, 17.44, -4.8, -0.4
  1.0: 33.21, 36.23, 36.86, -9.9, -1.7
  1.5: 49.81, 56.62, 58.75, -15.2, -3.6
  2.0: 66.41, 78.52, 83.58, -20.5, -6.1
  3.0: 99.62, 126.85, 142.40, -30.0, -10.9
Accuracy, tax on power+industry at rate r: r, linear, second, exact, err lin %, err 2nd %
  30: 28.36, 27.21, 27.23, +4.2, -0.1
  60: 56.73, 52.10, 52.38, +8.3, -0.5
  100: 94.55, 81.70, 83.19, +13.7, -1.8
  150: 141.82, 112.90, 118.24, +19.9, -4.5
Linear error below 5% for mix scale k <= 0.5 (exact TECP 17.4)

Horizon TECP (lambda_int 0.07, lambda_ext 0.35; credit price held at its long-run value):
  T=1: tax lin 26.45 exact 25.40; subsidy lin 1.00 exact 1.16; standard lin 0.87 exact 0.79; mix lin 28.33 exact 28.28
  T=5: tax lin 27.12 exact 26.01; subsidy lin 1.94 exact 2.26; standard lin 0.97 exact 0.94; mix lin 30.04 exact 30.96
  T=10: tax lin 27.65 exact 26.54; subsidy lin 2.67 exact 3.12; standard lin 1.05 exact 1.05; mix lin 31.37 exact 33.23
  T=20: tax lin 28.09 exact 26.98; subsidy lin 3.29 exact 3.87; standard lin 1.12 exact 1.13; mix lin 32.50 exact 35.35
  T=30: tax lin 28.24 exact 27.13; subsidy lin 3.51 exact 4.13; standard lin 1.14 exact 1.16; mix lin 32.90 exact 36.17
  T=0 limit (first order): tax 26.45; subsidy 1.00; standard 0.87; mix 28.33
  omega (LR switching share) 0.740; omega_1 0.363

Monte Carlo, 2000 draws, seed 20261029. Long run:
  mix_lin: median 32.4, 5th 31.3, 95th 33.4
  mix_exact: median 35.3, 5th 32.4, 95th 38.1
  tax_exact: median 27.1, 5th 26.0, 95th 28.2
  subsidy_exact: median 3.6, 5th 2.5, 95th 4.7
  standard_exact: median 0.9, 5th 0.7, 95th 1.1
  lambda: median 237.0, 5th 171.1, 95th 381.6
Short run (one year; adjustment speeds drawn):
  mix_lin: median 29.3, 5th 27.8, 95th 31.1
  mix_exact: median 27.2, 5th 23.2, 95th 31.4
  tax_exact: median 25.9, 5th 24.0, 95th 27.5
  subsidy_exact: median 0.5, 5th -0.6, 95th 1.8
  standard_exact: median 0.4, 5th -0.9, 95th 1.2
  lambda: median 600.0, 5th 600.0, 95th 600.0
  share of LR draws with mix TECP > explicit metric: 1.000
  LR ratio exact/linear: median 1.088, 5th 1.037, 95th 1.139
Central case, one year: mix lin 30.61, exact 28.69; tax 25.40; subsidy 1.16; standard 1.10 (credit price 600)

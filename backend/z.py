import csv

dates = ['08/10/2010','15/10/2010','22/10/2010','29/10/2010','05/11/2010','12/11/2010','19/11/2010','26/11/2010','30/11/2010','03/12/2010','10/12/2010','17/12/2010','23/12/2010','31/12/2010','10/01/2011','17/01/2011','24/01/2011','28/01/2011','31/01/2011','07/02/2011','14/02/2011','21/02/2011','25/02/2011','28/02/2011','04/03/2011','11/03/2011','18/03/2011','25/03/2011','31/03/2011','01/04/2011','11/04/2011','18/04/2011','25/04/2011','02/05/2011','09/05/2011','16/05/2011','23/05/2011','30/05/2011','06/06/2011','13/06/2011','20/06/2011','27/06/2011','30/06/2011','08/07/2011','18/07/2011','25/07/2011','31/07/2011','08/08/2011','15/08/2011','22/08/2011','31/08/2011','12/09/2011','20/09/2011','26/09/2011','03/10/2011','10/10/2011','17/10/2011','24/10/2011','31/10/2011','07/11/2011','14/11/2011','21/11/2011','28/11/2011','05/12/2011','12/12/2011','19/12/2011','23/12/2011','30/12/2011','09/01/2012','16/01/2012','23/01/2012','30/01/2012','06/02/2012','10/02/2012','20/02/2012','27/02/2012','05/03/2012','12/03/2012','19/03/2012','26/03/2012','02/04/2012','10/04/2012','16/04/2012','23/04/2012','30/04/2012','07/05/2012','14/05/2012','21/05/2012','28/05/2012','04/06/2012','11/06/2012','18/06/2012','25/06/2012','02/07/2012','09/07/2012','16/07/2012','23/07/2012','30/07/2012','01/08/2012','06/08/2012','13/08/2012','20/08/2012','27/08/2012','03/09/2012','10/09/2012','17/09/2012','24/09/2012','01/10/2012','08/10/2012','15/10/2012','22/10/2012','29/10/2012','05/11/2012','09/11/2012','19/11/2012','26/11/2012','03/12/2012','10/12/2012','17/12/2012','24/12/2012','31/12/2012','07/01/2013','14/01/2013','21/01/2013','28/01/2013','04/02/2013','11/02/2013','18/02/2013','25/02/2013','01/03/2013','11/03/2013','18/03/2013','25/03/2013','01/04/2013','08/04/2013','15/04/2013','22/04/2013','29/04/2013','04/05/2013','06/05/2013','14/05/2013','21/05/2013','27/05/2013','03/06/2013','10/06/2013','17/06/2013','24/06/2013','01/07/2013','08/07/2013','15/07/2013','22/07/2013','29/07/2013','05/08/2013','12/08/2013','19/08/2013','26/08/2013','02/09/2013','09/09/2013','16/09/2013','23/09/2013','30/09/2013','07/10/2013','14/10/2013','21/10/2013','28/10/2013','04/11/2013','11/11/2013','18/11/2013','25/11/2013','02/12/2013','09/12/2013','16/12/2013','23/12/2013','30/12/2013','06/01/2014','13/01/2014','20/01/2014','27/01/2014','03/02/2014','10/02/2014','17/02/2014','24/02/2014','03/03/2014','10/03/2014','17/03/2014','24/03/2014','31/03/2014','07/04/2014','14/04/2014','21/04/2014','28/04/2014','05/05/2014','12/05/2014','19/05/2014','26/05/2014','02/06/2014','10/06/2014','16/06/2014','23/06/2014','30/06/2014','07/07/2014','14/07/2014','21/07/2014','28/07/2014','04/08/2014','11/08/2014','18/08/2014','25/08/2014','01/09/2014','08/09/2014','15/09/2014','22/09/2014','29/09/2014','06/10/2014','13/10/2014','20/10/2014','27/10/2014','03/11/2014','10/11/2014','17/11/2014','24/11/2014','01/12/2014','08/12/2014','15/12/2014','22/12/2014','29/12/2014','05/01/2015','12/01/2015','19/01/2015','26/01/2015','02/02/2015','09/02/2015','16/02/2015','23/02/2015','02/03/2015','09/03/2015','16/03/2015','23/03/2015','30/03/2015','06/04/2015','14/04/2015','20/04/2015','27/04/2015','04/05/2015','11/05/2015','18/05/2015','26/05/2015','01/06/2015','08/06/2015','15/06/2015','22/06/2015','29/06/2015','06/07/2015','13/07/2015','20/07/2015','27/07/2015','03/08/2015','10/08/2015','17/08/2015','24/08/2015','31/08/2015','07/09/2015','14/09/2015','21/09/2015','28/09/2015','05/10/2015','12/10/2015','19/10/2015','26/10/2015','02/11/2015','09/11/2015','16/11/2015','25/11/2015','30/11/2015','07/12/2015','14/12/2015','21/12/2015','31/12/2015','11/01/2016','19/01/2016','25/01/2016','01/02/2016','08/02/2016','15/02/2016','22/02/2016','01/03/2016','07/03/2016','14/03/2016','21/03/2016','29/03/2016','04/04/2016','11/04/2016','18/04/2016','25/04/2016','02/05/2016','09/05/2016','16/05/2016','23/05/2016','30/05/2016','06/06/2016','13/06/2016','20/06/2016','27/06/2016','04/07/2016','11/07/2016','18/07/2016','25/07/2016','02/08/2016','08/08/2016','15/08/2016','22/08/2016','29/08/2016','05/09/2016','12/09/2016','19/09/2016','26/09/2016','03/10/2016','10/10/2016','17/10/2016','24/10/2016','31/10/2016','07/11/2016','14/11/2016','21/11/2016','28/11/2016','05/12/2016','12/12/2016','19/12/2016','02/01/2017','09/01/2017','16/01/2017','23/01/2017','30/01/2017','06/02/2017','13/02/2017','20/02/2017','27/02/2017','06/03/2017','13/03/2017','20/03/2017','27/03/2017','03/04/2017','10/04/2017','17/04/2017','24/04/2017','28/04/2017','08/05/2017','15/05/2017','22/05/2017','29/05/2017','05/06/2017','12/06/2017','19/06/2017','26/06/2017','03/07/2017','10/07/2017','17/07/2017','24/07/2017','31/07/2017','07/08/2017','14/08/2017','21/08/2017','28/08/2017','01/09/2017','11/09/2017','18/09/2017','25/09/2017','29/09/2017','09/10/2017','16/10/2017','23/10/2017','30/10/2017','06/11/2017','14/11/2017','20/11/2017','27/11/2017','04/12/2017','11/12/2017','18/12/2017','26/12/2017','31/12/2017','08/01/2018','15/01/2018','22/01/2018','29/01/2018','05/02/2018','12/02/2018','19/02/2018','26/02/2018','05/03/2018','12/03/2018','19/03/2018','26/03/2018','30/03/2018','09/04/2018','16/04/2018','23/04/2018','30/04/2018','07/05/2018','14/05/2018','21/05/2018','28/05/2018','04/06/2018','11/06/2018','18/06/2018','25/06/2018','02/07/2018','09/07/2018','16/07/2018','23/07/2018','30/07/2018','06/08/2018','14/08/2018','20/08/2018','27/08/2018','31/08/2018','10/09/2018','17/09/2018','24/09/2018','28/09/2018','08/10/2018','15/10/2018','22/10/2018','29/10/2018','05/11/2018','12/11/2018','19/11/2018','26/11/2018','30/11/2018','10/12/2018','17/12/2018','24/12/2018','31/12/2018','07/01/2019','14/01/2019','21/01/2019','28/01/2019','04/02/2019','11/02/2019','18/02/2019','25/02/2019','04/03/2019','11/03/2019','18/03/2019','25/03/2019','29/03/2019','08/04/2019','15/04/2019','23/04/2019','29/04/2019','06/05/2019','13/05/2019','20/05/2019','27/05/2019','31/05/2019','11/06/2019','17/06/2019','24/06/2019','08/07/2019','15/07/2019','22/07/2019','29/07/2019','05/08/2019','12/08/2019','19/08/2019','26/08/2019','30/08/2019','09/09/2019','16/09/2019','23/09/2019','30/09/2019','07/10/2019','14/10/2019','21/10/2019','28/10/2019','01/11/2019','08/11/2019','15/11/2019','25/11/2019','29/11/2019','09/12/2019','16/12/2019','23/12/2019','30/12/2019','06/01/2020','14/01/2020','20/01/2020','27/01/2020','03/02/2020','10/02/2020','17/02/2020','24/02/2020','28/02/2020','10/03/2020','16/03/2020','23/03/2020','30/03/2020','06/04/2020','10/04/2020','19/04/2020','27/04/2020','04/05/2020','11/05/2020','18/05/2020','25/05/2020','29/05/2020','05/06/2020','12/06/2020','19/06/2020','26/06/2020','03/07/2020','10/07/2020','17/07/2020','24/07/2020','31/07/2020','07/08/2020','14/08/2020','21/08/2020','28/08/2020','04/09/2020','11/09/2020','18/09/2020','25/09/2020','02/10/2020','09/10/2020','16/10/2020','23/10/2020','30/10/2020','06/11/2020','14/11/2020','20/11/2020','27/11/2020','04/12/2020','11/12/2020','18/12/2020','31/12/2020','08/01/2021','15/01/2021','22/01/2021','29/01/2021','05/02/2021','12/02/2021','26/02/2021','05/03/2021','12/03/2021','19/03/2021','26/03/2021','02/04/2021','09/04/2021','16/04/2021','23/04/2021','30/04/2021','07/05/2021','14/05/2021','21/05/2021','28/05/2021','04/06/2021','11/06/2021','18/06/2021','25/06/2021','02/07/2021','09/07/2021','16/07/2021','23/07/2021','30/07/2021','06/08/2021','13/08/2021','20/08/2021','27/08/2021','03/09/2021','10/09/2021','17/09/2021','24/09/2021','01/10/2021','08/10/2021','15/10/2021','22/10/2021','29/10/2021','05/11/2021','12/11/2021','19/11/2021','26/11/2021','03/12/2021','10/12/2021','17/12/2021','31/12/2021','07/01/2022','14/01/2022','21/01/2022','28/01/2022','04/02/2022','11/02/2022','18/02/2022','25/02/2022','04/03/2022','11/03/2022','18/03/2022','25/03/2022','01/04/2022','08/04/2022','15/04/2022','22/04/2022','29/04/2022','06/05/2022','13/05/2022','20/05/2022','27/05/2022','03/06/2022','10/06/2022','17/06/2022','24/06/2022','01/07/2022','08/07/2022','15/07/2022','22/07/2022','29/07/2022','05/08/2022','12/08/2022','19/08/2022','26/08/2022','02/09/2022','09/09/2022','16/09/2022','23/09/2022','30/09/2022','07/10/2022','14/10/2022','21/10/2022','28/10/2022','04/11/2022','11/11/2022','18/11/2022','25/11/2022','02/12/2022','09/12/2022','16/12/2022','31/12/2022','06/01/2023','13/01/2023','20/01/2023','27/01/2023','03/02/2023','10/02/2023','17/02/2023','24/02/2023','03/03/2023','10/03/2023','17/03/2023','24/03/2023','31/03/2023','07/04/2023','14/04/2023','21/04/2023','28/04/2023','05/05/2023','12/05/2023','19/05/2023','26/05/2023','02/06/2023','09/06/2023','16/06/2023','23/06/2023','30/06/2023','07/07/2023','14/07/2023','21/07/2023','28/07/2023','04/08/2023','11/08/2023','18/08/2023','25/08/2023','01/09/2023','08/09/2023','15/09/2023','22/09/2023','29/09/2023','06/10/2023','13/10/2023','20/10/2023','27/10/2023','03/11/2023','10/11/2023','17/11/2023','24/11/2023','01/12/2023','08/12/2023','15/12/2023','22/12/2023','29/12/2023','05/01/2024','12/01/2024','19/01/2024','26/01/2024','02/02/2024','09/02/2024','16/02/2024','23/02/2024','01/03/2024','08/03/2024','15/03/2024','22/03/2024','29/03/2024', '05/04/2024', '12/04/2024', '19/04/2024', '26/04/2024', '03/05/2024', '10/05/2024', '17/05/2024', '24/05/2024', '31/05/2024', '07/06/2024', '14/06/2024', '21/06/2024', '28/06/2024', '05/07/2024', '12/07/2024', '19/07/2024', '26/07/2024', '02/08/2024', '09/08/2024', '16/08/2024', '23/08/2024', '30/08/2024', '06/09/2024', '13/09/2024', '20/09/2024', '27/09/2024', '04/10/2024', '11/10/2024', '18/10/2024', '25/10/2024']

collat_yield = [0.12, 0.14, 0.13, 0.12, 0.12, 0.13, 0.14, 0.16, 0.17, 0.14, 0.12, 0.11, 0.14, 0.13, 0.14, 0.15, 0.16, 0.15, 0.15, 0.15, 0.12, 0.09, 0.13, 0.14, 0.12, 0.07, 0.07, 0.09, 0.09, 0.06, 0.04, 0.05, 0.05, 0.03, 0.01, 0.02, 0.05, 0.05, 0.03, 0.04, 0.02, 0.02, 0.02, 0.03, 0.01, 0.04, 0.09, 0.02, 0, 0, 0.01, 0.01, 0.01, 0, 0, 0.01, 0.02, 0.01, -0.01, 0, 0.01, 0.01, 0.01, 0, 0, 0, 0, 0.01, 0.01, 0.02, 0.04, 0.05, 0.07, 0.08, 0.08, 0.1, 0.06, 0.08, 0.08, 0.08, 0.06, 0.08, 0.08, 0.08, 0.09, 0.08, 0.09, 0.07, 0.08, 0.07, 0.08, 0.08, 0.08, 0.07, 0.07, 0.09, 0.09, 0.1, 0.09, 0.08, 0.1, 0.09, 0.09, 0.07, 0.1, 0.09, 0.1, 0.08, 0.1, 0.09, 0.09, 0.11, 0.09, 0.09, 0.08, 0.09, 0.08, 0.08, 0.02, 0.05, 0.04, 0.06, 0.07, 0.07, 0.06, 0.06, 0.07, 0.1, 0.12, 0.1, 0.09, 0.07, 0.06, 0.05, 0.06, 0.06, 0.05, 0.05, 0.05, 0.03, 0.04, 0.04, 0.04, 0.03, 0.04, 0.04, 0.04, 0.01, 0.03, 0.02, 0.01, 0.02, 0.04, 0.05, 0.04, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01, 0.02, 0.06, 0.03, 0.02, 0.04, 0.05, 0.07, 0.06, 0.05, 0.06, 0.06, 0.06, 0.06, 0.05, 0.03, 0.03, 0.05, 0.03, 0.06, 0.02, 0.04, 0.05, 0.04, 0.05, 0.05, 0.03, 0.03, 0.03, 0.03, 0.01, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03, 0.03, 0.01, 0.02, 0.01, 0.02, 0.02, 0.03, 0.02, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0, 0.01, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.02, 0.01, 0.01, 0.03, 0, 0.02, 0.01, 0.02, 0.01, 0.01, 0, 0.01, 0.01, 0.01, 0, 0.01, 0.01, 0, 0, 0.01, -0.01, 0.02, 0.03, 0.07, 0.07, 0.06, 0.02, 0, 0.03, 0.03, -0.01, 0, -0.01, 0, 0, 0.02, 0.06, 0.08, 0.1, 0.18, 0.17, 0.23, 0.21, 0.16, 0.17, 0.19, 0.24, 0.29, 0.3, 0.27, 0.28, 0.3, 0.33, 0.28, 0.32, 0.3, 0.23, 0.2, 0.22, 0.21, 0.25, 0.19, 0.22, 0.27, 0.32, 0.31, 0.26, 0.26, 0.25, 0.25, 0.26, 0.28, 0.3, 0.31, 0.27, 0.26, 0.29, 0.29, 0.31, 0.32, 0.36, 0.25, 0.19, 0.3, 0.32, 0.3, 0.32, 0.3, 0.41, 0.52, 0.43, 0.46, 0.46, 0.51, 0.49, 0.5, 0.5, 0.53, 0.49, 0.51, 0.52, 0.54, 0.52, 0.51, 0.72, 0.74, 0.73, 0.78, 0.76, 0.81, 0.81, 0.79, 0.8, 0.89, 0.88, 0.9, 0.93, 0.97, 1, 1, 0.95, 1.03, 1.03, 1.04, 1.17, 1.08, 1.05, 1.03, 0.98, 1.03, 1.01, 1.04, 1.02, 1.01, 1.05, 1.07, 1.07, 1.09, 1.1, 1.18, 1.24, 1.26, 1.25, 1.27, 1.29, 1.34, 1.34, 1.38, 1.41, 1.44, 1.42, 1.41, 1.48, 1.58, 1.59, 1.64, 1.66, 1.68, 1.76, 1.74, 1.71, 1.71, 1.74, 1.82, 1.8, 1.83, 1.9, 1.9, 1.89, 1.91, 1.9, 1.92, 1.89, 1.93, 1.96, 1.98, 1.96, 1.99, 2.01, 2.07, 2.04, 2.1, 2.1, 2.13, 2.15, 2.17, 2.2, 2.21, 2.28, 2.31, 2.31, 2.32, 2.35, 2.35, 2.4, 2.35, 2.38, 2.39, 2.38, 2.36, 2.41, 2.42, 2.4, 2.39, 2.38, 2.43, 2.42, 2.45, 2.43, 2.43, 2.44, 2.45, 2.39, 2.42, 2.41, 2.43, 2.41, 2.41, 2.4, 2.37, 2.34, 2.34, 2.25, 2.18, 2.11, 2.23, 2.13, 2.07, 2.1, 2.01, 1.98, 1.9, 1.98, 1.98, 1.95, 1.98, 1.89, 1.82, 1.71, 1.67, 1.66, 1.64, 1.52, 1.55, 1.56, 1.59, 1.58, 1.54, 1.56, 1.56, 1.53, 1.53, 1.56, 1.56, 1.54, 1.56, 1.56, 1.57, 1.54, 1.28, 0.46, 0.21, -0.01, 0.04, 0.09, 0.22, 0.11, 0.11, 0.1, 0.11, 0.11, 0.12, 0.14, 0.15, 0.16, 0.15, 0.14, 0.14, 0.13, 0.11, 0.11, 0.09, 0.09, 0.09, 0.09, 0.1, 0.11, 0.11, 0.09, 0.1, 0.09, 0.1, 0.09, 0.09, 0.09, 0.09, 0.09, 0.07, 0.08, 0.08, 0.07, 0.08, 0.07, 0.08, 0.08, 0.07, 0.05, 0.03, 0.04, 0.04, 0.03, 0.03, 0.01, 0.02, 0.02, 0.01, 0.01, 0.02, 0.01, 0.01, 0.01, 0, 0.01, 0.02, 0.02, 0.04, 0.05, 0.04, 0.05, 0.05, 0.05, 0.04, 0.05, 0.05, 0.05, 0.05, 0.04, 0.04, 0.04, 0.03, 0.04, 0.06, 0.05, 0.06, 0.06, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.04, 0.04, 0.1, 0.12, 0.17, 0.19, 0.23, 0.36, 0.34, 0.32, 0.33, 0.38, 0.39, 0.53, 0.52, 0.69, 0.77, 0.81, 0.83, 0.84, 0.98, 1.02, 1.06, 1.17, 1.34, 1.6, 1.66, 1.66, 1.91, 2.34, 2.42, 2.36, 2.5, 2.55, 2.67, 2.83, 2.89, 3.03, 3.13, 3.19, 3.27, 3.36, 3.72, 3.99, 4.07, 4.11, 4.17, 4.24, 4.29, 4.28, 4.28, 4.28, 4.37, 4.61, 4.6, 4.65, 4.67, 4.65, 4.76, 4.8, 4.81, 4.85, 4.91, 4.4, 4.65, 4.75, 4.86, 5.05, 5.07, 5.06, 5.22, 5.17, 5.24, 5.26, 5.37, 5.25, 5.22, 5.3, 5.3, 5.36, 5.39, 5.41, 5.42, 5.4, 5.43, 5.44, 5.48, 5.42, 5.46, 5.46, 5.48, 5.45, 5.51, 5.49, 5.46, 5.46, 5.41, 5.41, 5.39, 5.41, 5.37, 5.38, 5.39, 5.37, 5.34, 5.38, 5.37, 5.35, 5.36, 5.37, 5.38, 5.38, 5.41, 5.38, 5.39, 5.4, 5.38, 5.37, 5.37, 5.39, 5.41, 5.40, 5.40, 5.40, 5.40, 5.41, 5.41, 5.40, 5.39, 5.39, 5.36, 5.38, 5.34, 5.33, 5.30, 5.18, 5.22, 5.21, 5.13, 5.12, 5.06, 4.89, 4.66, 4.61, 4.62, 4.63, 4.63, 4.64]
insurance_risk = [5.81, 5.71, 5.6, 5.41, 5.39, 5.3, 5.36, 5.24, 5.41, 5.38, 5.48, 5.55, 5.53, 5.57, 5.5, 5.42, 5.36, 5.37, 5.25, 5.23, 5.27, 5.63, 5.61, 5.59, 5.5, 5.86, 8.93, 6.8, 6.94, 6.41, 6.75, 6.79, 6.74, 6.58, 6.59, 6.58, 6.55, 6.61, 6.48, 6.51, 6.55, 6.37, 6.4, 6.37, 6.36, 6.32, 6.26, 6.19, 6.4, 6.1, 6.12, 5.96, 5.86, 5.78, 5.35, 5.22, 5.11, 5, 4.98, 5, 5.19, 5.18, 5.08, 5.46, 5.41, 5.76, 5.99, 5.98, 5.98, 6.12, 6.13, 6.21, 6.33, 6.35, 6.42, 6.41, 6.57, 6.56, 6.57, 7.01, 7.04, 7.13, 7.13, 7.4, 8.37, 8.34, 8.34, 8.31, 8.33, 8.28, 8.08, 8.03, 7.95, 7.69, 7.67, 7.63, 7.64, 7.59, 7.39, 7.36, 7.29, 7.21, 7.11, 6.95, 6.82, 6.64, 6.47, 6.32, 6.13, 6.06, 5.87, 6.19, 7.18, 7.19, 7.21, 6.93, 6.9, 6.81, 6.65, 6.6, 6.65, 6.59, 6.74, 6.72, 6.65, 6.64, 6.61, 6.47, 6.36, 6.27, 6.16, 6.05, 5.96, 5.88, 5.85, 5.98, 5.87, 5.73, 5.52, 5.56, 5.55, 5.57, 5.67, 5.67, 5.82, 5.82, 5.83, 5.81, 5.7, 5.78, 5.76, 5.76, 5.69, 5.66, 5.58, 5.47, 5.3, 5.17, 5, 4.86, 4.69, 4.54, 4.44, 4.35, 4.28, 4.31, 4.28, 4.24, 4.22, 4.2, 4.26, 4.24, 4.26, 4.32, 4.3, 4.36, 4.38, 4.45, 4.41, 4.41, 4.37, 4.35, 4.36, 4.31, 4.29, 4.29, 4.25, 4.19, 4.25, 4.22, 4.45, 4.61, 4.54, 4.58, 4.65, 4.67, 4.66, 4.67, 4.7, 4.72, 4.73, 4.74, 4.71, 4.67, 4.66, 4.59, 4.55, 4.46, 4.37, 4.26, 4.13, 4.21, 4.11, 3.99, 3.92, 3.86, 3.81, 3.75, 3.74, 3.74, 3.77, 3.77, 3.81, 3.94, 3.97, 3.83, 3.75, 4, 4.02, 4.03, 4.19, 4.21, 4.25, 4.36, 4.4, 4.38, 4.41, 4.47, 4.51, 4.54, 4.63, 4.74, 4.71, 4.72, 4.82, 4.82, 4.85, 4.91, 4.92, 4.97, 4.94, 5.05, 5.04, 5.03, 5.05, 5, 4.94, 4.89, 4.88, 4.79, 4.71, 4.57, 4.46, 4.29, 4.16, 4.05, 4.01, 3.94, 3.94, 3.96, 3.95, 4.07, 4.1, 4.11, 4.11, 4.15, 4.18, 4.25, 4.26, 4.34, 4.44, 4.44, 4.44, 4.43, 4.43, 4.48, 4.48, 4.52, 4.51, 4.45, 4.42, 4.4, 4.43, 4.45, 4.41, 4.42, 4.51, 4.56, 4.55, 4.49, 4.57, 4.77, 4.69, 4.69, 4.7, 4.65, 4.59, 4.53, 4.47, 4.42, 4.33, 4.23, 4.07, 3.94, 3.81, 3.69, 3.6, 4.07, 3.47, 3.42, 3.37, 3.31, 3.3, 3.35, 3.33, 3.36, 3.4, 3.42, 3.65, 3.5, 3.83, 3.79, 3.73, 3.72, 3.7, 3.68, 3.67, 3.65, 3.63, 3.61, 3.61, 3.56, 3.54, 3.85, 3.86, 3.87, 4.24, 4.32, 4.36, 4.36, 4.34, 4.59, 4.53, 4.5, 4.48, 4.51, 4.53, 4.48, 4.41, 4.38, 4.34, 4.28, 4.4, 4.25, 9.29, 6.01, 6.62, 6.87, 6.63, 6.17, 6.1, 5.9, 5.94, 5.9, 6.01, 6.02, 5.55, 5.5, 5.64, 5.4, 5.39, 5.27, 5.21, 5.13, 5.09, 4.99, 5, 4.95, 4.79, 4.73, 4.71, 4.78, 4.6, 4.63, 4.51, 4.58, 4.6, 4.61, 4.7, 4.71, 4.75, 4.77, 4.79, 4.79, 4.77, 4.76, 4.73, 4.73, 4.77, 4.76, 4.83, 4.86, 4.86, 4.91, 5, 4.92, 4.88, 5.07, 4.9, 4.85, 4.85, 4.79, 4.81, 4.82, 4.66, 4.73, 4.76, 4.78, 5.19, 5.43, 5.61, 5.57, 5.62, 5.45, 5.57, 5.56, 5.43, 5.46, 5.46, 5.64, 5.6, 5.35, 5.46, 5.52, 5.55, 5.37, 5.4, 5.43, 5.51, 5.54, 5.62, 5.71, 5.88, 6.02, 6.09, 5.93, 6.09, 6.12, 6.13, 6.1, 6.04, 5.97, 5.97, 5.84, 5.74, 5.63, 6.25, 5.64, 5.38, 5.41, 5.33, 5.2, 5.15, 4.82, 4.94, 4.91, 4.88, 4.67, 5.09, 5.09, 5.06, 5.49, 5.5, 5.48, 5.5, 5.46, 5.73, 5.64, 5.52, 5.48, 5.58, 5.67, 5.49, 5.49, 5.5, 6.1, 6.34, 6.83, 6.88, 6.85, 6.83, 6.91, 6.87, 6.99, 6.98, 7.32, 7.13, 7.13, 7.11, 7.09, 7.13, 7.16, 6.96, 6.82, 6.74, 6.65, 6.48, 6.35, 6.19, 6.03, 5.88, 5.7, 5.56, 5.53, 5.53, 5.44, 5.44, 5.48, 5.25, 5.34, 5.46, 5.44, 5.55, 5.7, 5.53, 5.5, 5.68, 5.75, 5.72, 5.61, 5.57, 5.55, 6.33, 6.01, 5.99, 5.87, 5.72, 5.57, 5.64, 5.69, 5.79, 5.77, 5.79, 5.75, 5.69, 5.67, 5.67, 5.76, 5.75, 5.69, 5.67, 5.62, 5.62, 5.65, 5.61, 5.65, 5.62, 5.57, 5.51, 5.71, 5.65, 5.85, 5.58, 5.32, 5.26, 5.3, 5.31, 5.17, 5.12, 5.18, 5.13, 5.11, 5.07, 5.21, 5.29, 5.33, 5.4, 5.5, 5.55, 5.65, 5.65, 5.66, 5.78, 5.95, 5.77, 5.91, 5.88, 5.95, 5.99, 6.15, 6.04, 6.24, 6.29, 6.39, 6.42, 6.46, 6.56, 6.67, 7.02, 7.05, 7.13, 7.34, 7.4, 7.45, 7.47, 7.49, 7.47, 7.46, 7.39, 7.33, 7.23, 7.16, 7.04, 6.91, 9.34, 9.01, 9.16, 9.19, 9.53, 10, 10.42, 10.85, 10.92, 10.96, 10.99, 10.95, 11.03, 11.17, 11.31, 11.18, 11.02, 10.78, 10.67, 10.63, 10.52, 10.55, 10.55, 10.29, 10.2, 10.07, 10, 9.85, 9.66, 9.48, 9.53, 9.48, 9.32, 9.34, 9.29, 9.57, 9.45, 9.25, 9.14, 9.02, 8.85, 8.74, 8.72, 8.69, 8.58, 8.46, 8.27, 8.14, 8.12, 8.11, 8.06, 7.8, 7.55, 7.44, 7.24, 7.18, 6.87, 6.83, 6.7, 6.64, 6.65, 6.94, 7.04, 7.04, 6.99, 7, 7.12, 7.23, 7.12, 7.03, 7.02, 6.95, 6.92, 6.92, 6.68, 6.69, 6.67, 6.62, 6.94, 6.93, 7.12, 7.18, 7.38, 7.43, 7.73, 8.05, 8.13, 8.43, 8.39, 8.38, 8.33, 8.41, 8.42, 8.37, 8.24, 8.11, 7.97, 7.78, 7.61, 7.40, 7.22, 7.02, 6.68, 6.54, 6.39, 7.07, 6.84, 6.54]
expected_loss = [1.05, 1.05, 1.05, 1.16, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.32, 1.32, 1.32, 1.34, 1.45, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.48, 1.42, 1.42, 1.42, 1.39, 1.38, 1.39, 1.39, 1.39, 1.39, 1.39, 1.39, 1.37, 1.37, 1.37, 1.37, 1.37, 1.37, 1.37, 1.39, 1.39, 1.39, 1.39, 1.39, 1.39, 1.46, 1.44, 1.55, 1.55, 1.56, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.6, 1.6, 1.6, 1.6, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.68, 1.68, 1.67, 1.67, 1.67, 1.67, 1.68, 1.68, 1.68, 1.65, 1.65, 1.65, 1.65, 1.66, 1.66, 1.66, 1.66, 1.63, 1.63, 1.63, 1.6, 1.6, 1.6, 1.6, 1.61, 1.61, 1.61, 1.61, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.51, 1.51, 1.51, 1.56, 1.53, 1.58, 1.58, 1.5, 1.4, 1.49, 1.49, 1.48, 1.47, 1.51, 1.53, 1.52, 1.52, 1.51, 1.48, 1.48, 1.48, 1.48, 1.48, 1.5, 1.5, 1.5, 1.5, 1.48, 1.46, 1.46, 1.46, 1.46, 1.46, 1.44, 1.44, 1.4, 1.4, 1.4, 1.4, 1.4, 1.48, 1.48, 1.45, 1.48, 1.48, 1.48, 1.48, 1.47, 1.47, 1.48, 1.48, 1.47, 1.45, 1.42, 1.42, 1.39, 1.39, 1.39, 1.37, 1.37, 1.48, 1.4, 1.38, 1.38, 1.42, 1.4, 1.4, 1.4, 1.44, 1.44, 1.44, 1.44, 1.44, 1.44, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.43, 1.43, 1.43, 1.45, 1.45, 1.45, 1.45, 1.46, 1.46, 1.46, 1.57, 1.55, 1.55, 1.57, 1.57, 1.57, 1.57, 1.58, 1.57, 1.57, 1.58, 1.57, 1.55, 1.55, 1.55, 1.55, 1.57, 1.57, 1.57, 1.57, 1.56, 1.57, 1.57, 1.57, 1.56, 1.56, 1.56, 1.56, 1.55, 1.55, 1.55, 1.55, 1.57, 1.57, 1.57, 1.55, 1.55, 1.55, 1.55, 1.55, 1.55, 1.62, 1.63, 1.63, 1.63, 1.63, 1.6, 1.58, 1.58, 1.57, 1.59, 1.58, 1.58, 1.58, 1.58, 1.59, 1.59, 1.61, 1.6, 1.6, 1.58, 1.59, 1.61, 1.62, 1.62, 1.65, 1.64, 1.65, 1.66, 1.66, 1.66, 1.73, 1.73, 1.73, 1.73, 1.72, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.76, 1.76, 1.76, 1.73, 1.72, 1.73, 1.73, 1.73, 1.73, 1.73, 1.75, 1.75, 1.76, 1.77, 1.79, 1.83, 1.84, 2, 2, 1.99, 1.99, 1.99, 1.99, 1.98, 1.98, 1.99, 1.99, 1.99, 1.93, 1.93, 2.09, 2.08, 2.08, 2.06, 2.08, 2.09, 2.09, 2.07, 2.09, 2.06, 2.06, 2.09, 2.13, 2.13, 2.13, 2.13, 2.16, 2.17, 2.17, 2.16, 2.17, 1.97, 2.04, 2.06, 2.06, 2.08, 2.09, 2.09, 2.07, 2.07, 2.07, 2.12, 2.12, 2.14, 2.12, 2.14, 2.14, 2.18, 2.19, 2.14, 2.14, 2.14, 2.13, 2.11, 2.12, 2.12, 2.08, 2.08, 2.1, 2.09, 2.03, 2.02, 2.05, 2.05, 2.02, 2.06, 2.07, 2.07, 2.06, 2.09, 2.08, 2.08, 2.08, 2.08, 2.1, 2.09, 2.09, 2.09, 2.14, 2.14, 2.14, 2.15, 2.15, 2.15, 2.14, 2.14, 2.14, 2.14, 2.13, 2.14, 2.14, 2.14, 2.14, 2.14, 2.13, 2.11, 2.11, 2.15, 2.15, 2.14, 2.15, 2.13, 2.17, 2.15, 2.15, 2.15, 2.15, 2.14, 2.14, 2.14, 2.15, 2.15, 2.14, 2.14, 2.14, 2.17, 2.17, 2.15, 2.15, 2.15, 2.14, 2.18, 2.18, 2.17, 2.19, 2.15, 2.15, 2.15, 2.15, 2.14, 2.14, 2.13, 2.13, 2.12, 2.13, 2.14, 2.14, 2.14, 2.14, 2.14, 2.14, 2.14, 2.14, 2.15, 2.15, 2.19, 2.2, 2.21, 2.29, 2.29, 2.29, 2.29, 2.29, 2.32, 2.32, 2.3, 2.29, 2.29, 2.31, 2.28, 2.29, 2.29, 2.3, 2.3, 2.3, 2.31, 2.31, 2.31, 2.32, 2.32, 2.33, 2.33, 2.31, 2.32, 2.31, 2.33, 2.36, 2.37, 2.34, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.37, 2.37, 2.38, 2.39, 2.39, 2.41, 2.41, 2.39, 2.38, 2.38, 2.36, 2.37, 2.4, 2.4, 2.4, 2.35, 2.36, 2.36, 2.37, 2.38, 2.38, 2.38, 2.37, 2.34, 2.45, 2.46, 2.46, 2.45, 2.45, 2.41, 2.44, 2.47, 2.42, 2.42, 2.43, 2.43, 2.39, 2.38, 2.38, 2.4, 2.41, 2.4, 2.4, 2.4, 2.4, 2.41, 2.41, 2.36, 2.36, 2.36, 2.36, 2.35, 2.35, 2.33, 2.35, 2.32, 2.32, 2.36, 2.37, 2.35, 2.35, 2.39, 2.39, 2.39, 2.38, 2.34, 2.35, 2.34, 2.36, 2.35, 2.34, 2.34, 2.34, 2.34, 2.39, 2.4, 2.4, 2.38, 2.38, 2.37, 2.33, 2.37, 2.37, 2.35, 2.36, 2.35, 2.33, 2.34, 2.32, 2.34, 2.35, 2.35, 2.35, 2.35, 2.34, 2.33, 2.33, 2.34, 2.34, 2.34, 2.34, 2.34, 2.34, 2.34, 2.34, 2.34, 2.25, 2.24, 2.24, 2.24, 2.25, 2.25, 2.29, 2.29, 2.3, 2.29, 2.29, 2.29, 2.28, 2.29, 2.31, 2.32, 2.32, 2.3, 2.29, 2.29, 2.29, 2.28, 2.31, 2.31, 2.31, 2.29, 2.25, 2.28, 2.26, 2.25, 2.24, 2.23, 2.22, 2.21, 2.18, 2.18, 2.18, 2.18, 2.17, 2.17, 2.13, 2.13, 2.13, 2.13, 2.13, 2.14, 2.14, 2.14, 2.14, 2.14, 2.14, 2.14, 2.15, 2.15, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.18, 2.17, 2.17, 2.16, 2.17, 2.17, 2.18, 2.18, 2.18, 2.18, 2.12, 2.17, 2.19, 2.2, 2.19, 2.18, 2.18, 2.18, 2.18, 2.18, 2.18, 2.18, 2.18, 2.18, 2.16, 2.15, 2.16, 2.19, 2.20, 2.19, 2.19, 2.19, 2.19, 2.19, 2.19, 2.18, 2.18, 2.19, 2.19, 2.19, 2.18, 2.18, 2.18, 2.19, 2.19]

print(dates[1])

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['Date', 'Y1', 'Y2', 'Y3'])
    
    # Write the data
    for i in range(len(dates)):
        writer.writerow([dates[i], collat_yield[i], insurance_risk[i], expected_loss[i]])

print("CSV file created successfully.")
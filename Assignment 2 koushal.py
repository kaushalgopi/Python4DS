{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "#%matplotlib notebook\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "import the dataset into a dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>EmployeeName</th>\n",
       "      <th>JobTitle</th>\n",
       "      <th>BasePay</th>\n",
       "      <th>OvertimePay</th>\n",
       "      <th>OtherPay</th>\n",
       "      <th>Benefits</th>\n",
       "      <th>TotalPay</th>\n",
       "      <th>TotalPayBenefits</th>\n",
       "      <th>Year</th>\n",
       "      <th>Notes</th>\n",
       "      <th>Agency</th>\n",
       "      <th>Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>NATHANIEL FORD</td>\n",
       "      <td>GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY</td>\n",
       "      <td>167411.18</td>\n",
       "      <td>0.00</td>\n",
       "      <td>400184.25</td>\n",
       "      <td>NaN</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>2011</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>GARY JIMENEZ</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>155966.02</td>\n",
       "      <td>245131.88</td>\n",
       "      <td>137811.38</td>\n",
       "      <td>NaN</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>2011</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>ALBERT PARDINI</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>212739.13</td>\n",
       "      <td>106088.18</td>\n",
       "      <td>16452.60</td>\n",
       "      <td>NaN</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>2011</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>CHRISTOPHER CHONG</td>\n",
       "      <td>WIRE ROPE CABLE MAINTENANCE MECHANIC</td>\n",
       "      <td>77916.00</td>\n",
       "      <td>56120.71</td>\n",
       "      <td>198306.90</td>\n",
       "      <td>NaN</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>2011</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>PATRICK GARDNER</td>\n",
       "      <td>DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)</td>\n",
       "      <td>134401.60</td>\n",
       "      <td>9737.00</td>\n",
       "      <td>182234.59</td>\n",
       "      <td>NaN</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>2011</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148649</th>\n",
       "      <td>148650</td>\n",
       "      <td>Roy I Tillery</td>\n",
       "      <td>Custodian</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148650</th>\n",
       "      <td>148651</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148651</th>\n",
       "      <td>148652</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148652</th>\n",
       "      <td>148653</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148653</th>\n",
       "      <td>148654</td>\n",
       "      <td>Joe Lopez</td>\n",
       "      <td>Counselor, Log Cabin Ranch</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>-618.13</td>\n",
       "      <td>0.0</td>\n",
       "      <td>-618.13</td>\n",
       "      <td>-618.13</td>\n",
       "      <td>2014</td>\n",
       "      <td>NaN</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>148654 rows × 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Id       EmployeeName  \\\n",
       "0            1     NATHANIEL FORD   \n",
       "1            2       GARY JIMENEZ   \n",
       "2            3     ALBERT PARDINI   \n",
       "3            4  CHRISTOPHER CHONG   \n",
       "4            5    PATRICK GARDNER   \n",
       "...        ...                ...   \n",
       "148649  148650      Roy I Tillery   \n",
       "148650  148651       Not provided   \n",
       "148651  148652       Not provided   \n",
       "148652  148653       Not provided   \n",
       "148653  148654          Joe Lopez   \n",
       "\n",
       "                                              JobTitle    BasePay  \\\n",
       "0       GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY  167411.18   \n",
       "1                      CAPTAIN III (POLICE DEPARTMENT)  155966.02   \n",
       "2                      CAPTAIN III (POLICE DEPARTMENT)  212739.13   \n",
       "3                 WIRE ROPE CABLE MAINTENANCE MECHANIC   77916.00   \n",
       "4         DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)  134401.60   \n",
       "...                                                ...        ...   \n",
       "148649                                       Custodian       0.00   \n",
       "148650                                    Not provided        NaN   \n",
       "148651                                    Not provided        NaN   \n",
       "148652                                    Not provided        NaN   \n",
       "148653                      Counselor, Log Cabin Ranch       0.00   \n",
       "\n",
       "        OvertimePay   OtherPay  Benefits   TotalPay  TotalPayBenefits  Year  \\\n",
       "0              0.00  400184.25       NaN  567595.43         567595.43  2011   \n",
       "1         245131.88  137811.38       NaN  538909.28         538909.28  2011   \n",
       "2         106088.18   16452.60       NaN  335279.91         335279.91  2011   \n",
       "3          56120.71  198306.90       NaN  332343.61         332343.61  2011   \n",
       "4           9737.00  182234.59       NaN  326373.19         326373.19  2011   \n",
       "...             ...        ...       ...        ...               ...   ...   \n",
       "148649         0.00       0.00       0.0       0.00              0.00  2014   \n",
       "148650          NaN        NaN       NaN       0.00              0.00  2014   \n",
       "148651          NaN        NaN       NaN       0.00              0.00  2014   \n",
       "148652          NaN        NaN       NaN       0.00              0.00  2014   \n",
       "148653         0.00    -618.13       0.0    -618.13           -618.13  2014   \n",
       "\n",
       "        Notes         Agency  Status  \n",
       "0         NaN  San Francisco     NaN  \n",
       "1         NaN  San Francisco     NaN  \n",
       "2         NaN  San Francisco     NaN  \n",
       "3         NaN  San Francisco     NaN  \n",
       "4         NaN  San Francisco     NaN  \n",
       "...       ...            ...     ...  \n",
       "148649    NaN  San Francisco     NaN  \n",
       "148650    NaN  San Francisco     NaN  \n",
       "148651    NaN  San Francisco     NaN  \n",
       "148652    NaN  San Francisco     NaN  \n",
       "148653    NaN  San Francisco     NaN  \n",
       "\n",
       "[148654 rows x 13 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"Salary.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "display the column names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: [Id, EmployeeName, JobTitle, BasePay, OvertimePay, OtherPay, Benefits, TotalPay, TotalPayBenefits, Year, Notes, Agency, Status]\n",
      "Index: []\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Index(['Id', 'EmployeeName', 'JobTitle', 'BasePay', 'OvertimePay', 'OtherPay',\n",
       "       'Benefits', 'TotalPay', 'TotalPayBenefits', 'Year', 'Notes', 'Agency',\n",
       "       'Status'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = df.columns\n",
    "print(df[:0]) # checking the column names in the row 1\n",
    "a"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "display the number of rows and cols"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(148654, 13)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "display the dataframe info (types of data in columns and not null values etc.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 148654 entries, 0 to 148653\n",
      "Data columns (total 13 columns):\n",
      " #   Column            Non-Null Count   Dtype  \n",
      "---  ------            --------------   -----  \n",
      " 0   Id                148654 non-null  int64  \n",
      " 1   EmployeeName      148654 non-null  object \n",
      " 2   JobTitle          148654 non-null  object \n",
      " 3   BasePay           148045 non-null  float64\n",
      " 4   OvertimePay       148650 non-null  float64\n",
      " 5   OtherPay          148650 non-null  float64\n",
      " 6   Benefits          112491 non-null  float64\n",
      " 7   TotalPay          148654 non-null  float64\n",
      " 8   TotalPayBenefits  148654 non-null  float64\n",
      " 9   Year              148654 non-null  int64  \n",
      " 10  Notes             0 non-null       float64\n",
      " 11  Agency            148654 non-null  object \n",
      " 12  Status            0 non-null       float64\n",
      "dtypes: float64(8), int64(2), object(3)\n",
      "memory usage: 14.7+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info() # (verbose=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "display stats of the dataframe like count, mean, std, max, 25% etc....."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>BasePay</th>\n",
       "      <th>OvertimePay</th>\n",
       "      <th>OtherPay</th>\n",
       "      <th>Benefits</th>\n",
       "      <th>TotalPay</th>\n",
       "      <th>TotalPayBenefits</th>\n",
       "      <th>Year</th>\n",
       "      <th>Notes</th>\n",
       "      <th>Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>148654.000000</td>\n",
       "      <td>148045.000000</td>\n",
       "      <td>148650.000000</td>\n",
       "      <td>148650.000000</td>\n",
       "      <td>112491.000000</td>\n",
       "      <td>148654.000000</td>\n",
       "      <td>148654.000000</td>\n",
       "      <td>148654.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>74327.500000</td>\n",
       "      <td>66325.448841</td>\n",
       "      <td>5066.059886</td>\n",
       "      <td>3648.767297</td>\n",
       "      <td>25007.893151</td>\n",
       "      <td>74768.321972</td>\n",
       "      <td>93692.554811</td>\n",
       "      <td>2012.522643</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>42912.857795</td>\n",
       "      <td>42764.635495</td>\n",
       "      <td>11454.380559</td>\n",
       "      <td>8056.601866</td>\n",
       "      <td>15402.215858</td>\n",
       "      <td>50517.005274</td>\n",
       "      <td>62793.533483</td>\n",
       "      <td>1.117538</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-166.010000</td>\n",
       "      <td>-0.010000</td>\n",
       "      <td>-7058.590000</td>\n",
       "      <td>-33.890000</td>\n",
       "      <td>-618.130000</td>\n",
       "      <td>-618.130000</td>\n",
       "      <td>2011.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>37164.250000</td>\n",
       "      <td>33588.200000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>11535.395000</td>\n",
       "      <td>36168.995000</td>\n",
       "      <td>44065.650000</td>\n",
       "      <td>2012.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>74327.500000</td>\n",
       "      <td>65007.450000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>811.270000</td>\n",
       "      <td>28628.620000</td>\n",
       "      <td>71426.610000</td>\n",
       "      <td>92404.090000</td>\n",
       "      <td>2013.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>111490.750000</td>\n",
       "      <td>94691.050000</td>\n",
       "      <td>4658.175000</td>\n",
       "      <td>4236.065000</td>\n",
       "      <td>35566.855000</td>\n",
       "      <td>105839.135000</td>\n",
       "      <td>132876.450000</td>\n",
       "      <td>2014.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>148654.000000</td>\n",
       "      <td>319275.010000</td>\n",
       "      <td>245131.880000</td>\n",
       "      <td>400184.250000</td>\n",
       "      <td>96570.660000</td>\n",
       "      <td>567595.430000</td>\n",
       "      <td>567595.430000</td>\n",
       "      <td>2014.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Id        BasePay    OvertimePay       OtherPay  \\\n",
       "count  148654.000000  148045.000000  148650.000000  148650.000000   \n",
       "mean    74327.500000   66325.448841    5066.059886    3648.767297   \n",
       "std     42912.857795   42764.635495   11454.380559    8056.601866   \n",
       "min         1.000000    -166.010000      -0.010000   -7058.590000   \n",
       "25%     37164.250000   33588.200000       0.000000       0.000000   \n",
       "50%     74327.500000   65007.450000       0.000000     811.270000   \n",
       "75%    111490.750000   94691.050000    4658.175000    4236.065000   \n",
       "max    148654.000000  319275.010000  245131.880000  400184.250000   \n",
       "\n",
       "            Benefits       TotalPay  TotalPayBenefits           Year  Notes  \\\n",
       "count  112491.000000  148654.000000     148654.000000  148654.000000    0.0   \n",
       "mean    25007.893151   74768.321972      93692.554811    2012.522643    NaN   \n",
       "std     15402.215858   50517.005274      62793.533483       1.117538    NaN   \n",
       "min       -33.890000    -618.130000       -618.130000    2011.000000    NaN   \n",
       "25%     11535.395000   36168.995000      44065.650000    2012.000000    NaN   \n",
       "50%     28628.620000   71426.610000      92404.090000    2013.000000    NaN   \n",
       "75%     35566.855000  105839.135000     132876.450000    2014.000000    NaN   \n",
       "max     96570.660000  567595.430000     567595.430000    2014.000000    NaN   \n",
       "\n",
       "       Status  \n",
       "count     0.0  \n",
       "mean      NaN  \n",
       "std       NaN  \n",
       "min       NaN  \n",
       "25%       NaN  \n",
       "50%       NaN  \n",
       "75%       NaN  \n",
       "max       NaN  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe() # statistics - Summary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "display null values per column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "BasePay           609\n",
       "OvertimePay         4\n",
       "OtherPay            4\n",
       "Benefits        36163\n",
       "Notes          148654\n",
       "Status         148654\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "null_values=df.columns[df.isnull().any()]\n",
    "df[null_values].isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "remove columns will all values as NaN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>EmployeeName</th>\n",
       "      <th>JobTitle</th>\n",
       "      <th>TotalPay</th>\n",
       "      <th>TotalPayBenefits</th>\n",
       "      <th>Year</th>\n",
       "      <th>Agency</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>NATHANIEL FORD</td>\n",
       "      <td>GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>567595.43</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>GARY JIMENEZ</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>538909.28</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>ALBERT PARDINI</td>\n",
       "      <td>CAPTAIN III (POLICE DEPARTMENT)</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>335279.91</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>CHRISTOPHER CHONG</td>\n",
       "      <td>WIRE ROPE CABLE MAINTENANCE MECHANIC</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>332343.61</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>PATRICK GARDNER</td>\n",
       "      <td>DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>326373.19</td>\n",
       "      <td>2011</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148649</th>\n",
       "      <td>148650</td>\n",
       "      <td>Roy I Tillery</td>\n",
       "      <td>Custodian</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148650</th>\n",
       "      <td>148651</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148651</th>\n",
       "      <td>148652</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148652</th>\n",
       "      <td>148653</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>Not provided</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2014</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148653</th>\n",
       "      <td>148654</td>\n",
       "      <td>Joe Lopez</td>\n",
       "      <td>Counselor, Log Cabin Ranch</td>\n",
       "      <td>-618.13</td>\n",
       "      <td>-618.13</td>\n",
       "      <td>2014</td>\n",
       "      <td>San Francisco</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>148654 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Id       EmployeeName  \\\n",
       "0            1     NATHANIEL FORD   \n",
       "1            2       GARY JIMENEZ   \n",
       "2            3     ALBERT PARDINI   \n",
       "3            4  CHRISTOPHER CHONG   \n",
       "4            5    PATRICK GARDNER   \n",
       "...        ...                ...   \n",
       "148649  148650      Roy I Tillery   \n",
       "148650  148651       Not provided   \n",
       "148651  148652       Not provided   \n",
       "148652  148653       Not provided   \n",
       "148653  148654          Joe Lopez   \n",
       "\n",
       "                                              JobTitle   TotalPay  \\\n",
       "0       GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY  567595.43   \n",
       "1                      CAPTAIN III (POLICE DEPARTMENT)  538909.28   \n",
       "2                      CAPTAIN III (POLICE DEPARTMENT)  335279.91   \n",
       "3                 WIRE ROPE CABLE MAINTENANCE MECHANIC  332343.61   \n",
       "4         DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)  326373.19   \n",
       "...                                                ...        ...   \n",
       "148649                                       Custodian       0.00   \n",
       "148650                                    Not provided       0.00   \n",
       "148651                                    Not provided       0.00   \n",
       "148652                                    Not provided       0.00   \n",
       "148653                      Counselor, Log Cabin Ranch    -618.13   \n",
       "\n",
       "        TotalPayBenefits  Year         Agency  \n",
       "0              567595.43  2011  San Francisco  \n",
       "1              538909.28  2011  San Francisco  \n",
       "2              335279.91  2011  San Francisco  \n",
       "3              332343.61  2011  San Francisco  \n",
       "4              326373.19  2011  San Francisco  \n",
       "...                  ...   ...            ...  \n",
       "148649              0.00  2014  San Francisco  \n",
       "148650              0.00  2014  San Francisco  \n",
       "148651              0.00  2014  San Francisco  \n",
       "148652              0.00  2014  San Francisco  \n",
       "148653           -618.13  2014  San Francisco  \n",
       "\n",
       "[148654 rows x 7 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = df.dropna(axis=1) # inplace = True\n",
    "df1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "display number of unique values in each column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Id                  148654\n",
       "EmployeeName        110811\n",
       "JobTitle              2159\n",
       "BasePay             109489\n",
       "OvertimePay          65998\n",
       "OtherPay             83225\n",
       "Benefits             98465\n",
       "TotalPay            138486\n",
       "TotalPayBenefits    142098\n",
       "Year                     4\n",
       "Notes                    0\n",
       "Agency                   1\n",
       "Status                   0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = pd.read_csv(\"Salary.csv\")\n",
    "df2.nunique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "mean of total pay of all people based on year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Year\n",
       "2011    71744.103871\n",
       "2012    74113.262265\n",
       "2013    77611.443142\n",
       "2014    75463.918140\n",
       "Name: TotalPay, dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftp = df2.groupby('Year').mean()['TotalPay']  #(total pay vs year))\n",
    "dftp"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "how many people have 0 overtime pay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "77321"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3 = sum(df2[df2['OvertimePay']==0]['Id'].value_counts()==1)\n",
    "df3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "max, min, mean, median and other stats of TotalPay of people having 0 OvertimePay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     77321.000000\n",
       "mean      60229.348901\n",
       "std       49307.912350\n",
       "min        -618.130000\n",
       "25%       13290.450000\n",
       "50%       58158.590000\n",
       "75%       91115.090000\n",
       "max      567595.430000\n",
       "Name: TotalPay, dtype: float64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Stats = df2.loc[df2['OvertimePay'] == 0]\n",
    "Stats['TotalPay'].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "find Id of that person with max TotalPay you got in previous question"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Id_person = df2.loc[df2['TotalPay'].idxmax()]\n",
    "Id_person['Id']\n",
    "#df2.groupby(['TotalPay']).max()['Id']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "name of employee with total pay benefits = 87619.78"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12345    REBECCA CHIU\n",
       "Name: EmployeeName, dtype: object"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Name_Emp = df1.loc[df1['TotalPayBenefits'] == 87619.78]\n",
    "Name_Emp['EmployeeName']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "how many people have BasePay > 150000 and OvertimePay > 100000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "156"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Total_people = df2[(df2['BasePay'] > 150000) & (df2['OvertimePay'] > 100000)]\n",
    "Total_people.size"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "which job title generally has highest average TotalPayBenefits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "JobTitle            ZOO CURATOR\n",
       "TotalPayBenefits         436224\n",
       "dtype: object"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Job_Title = df2.groupby('JobTitle', as_index = False)['TotalPayBenefits'].mean().max()\n",
    "Job_Title"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many employees are POLICE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2512"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[df2['JobTitle'].str.contains('POLICE')]['JobTitle'].size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "# How many employees are POLICE\n",
    "def police_string(title):\n",
    "    if 'police' in title.lower().split():\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total employees who are Police:  7489\n"
     ]
    }
   ],
   "source": [
    "P = sum(df2['JobTitle'].apply(lambda x:police_string(x)))\n",
    "print(\"Total employees who are Police: \",P)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

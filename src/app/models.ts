export interface AuthToken {
  access: string;
  refresh: string;
}
export interface User{
  id:string;
  name: string;
  surname: string;
  password: string;
  phone_number: string;
}
export interface UserTariff {
  id: number;
  user: number | User;
  tariff: number | TariffPlan;
}
export interface TariffPlan{
  id:string;
  name: string;
  price: number;
  data_limit: number;
  call_minutes: number;
  sms_count: number;
}


export interface TariffPlan {
    id: number;
    name: string;
    price: number;
    data_limit: number;
    call_minutes: number;
    sms_count: number;
    description: string;
    duration: number;
    is_active: boolean;
}


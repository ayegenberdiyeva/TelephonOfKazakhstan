export interface User {
    id: number;
    firstName: string;
    lastName: string;
    username: string;
    email: string;
    password: string;
    phone: string;
    is_active: boolean;
    is_superuser: boolean;
}

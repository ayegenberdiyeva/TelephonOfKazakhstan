import { ApplicationConfig } from '@angular/core';
import { provideRouter, Routes } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import {RegisterComponent } from './register/register.component';
import {TariffsComponent} from './tariffs/tariffs.component';
import {ContactsComponent} from './contact_us/contact_us.component';
import {ServicesComponent} from './services/services.component';
import {ProfileComponent} from './profile/profile.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'home', component: HomeComponent },
  { path: 'register', component: RegisterComponent },
  {path: 'tariffs', component: TariffsComponent },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'contacts', component: ContactsComponent },
  { path: 'services', component: ServicesComponent },
  { path: 'profile', component: ProfileComponent },
];

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient()
  ]
};

import { Component } from '@angular/core';
import {FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import {User} from '../models';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private router: Router
  ) {
    this.form = this.fb.group({
      name: [''],
      surname: [''],
      phone_number: [''],
      password: ['']
    });
  }

  submit() {
    if (this.form.valid) {
      const { phone_number, password, name, surname } = this.form.value;

      this.http.post('http://localhost:8000/api/register/', {
        username: phone_number,
        password,
        name,
        surname
      }).subscribe({
        next: () => {
          alert('Registered!');
          this.router.navigate(['/login']);
        },
        error: err => {
          console.error(err);
          alert('Registration failed!');
        }
      });
    }
  }

}


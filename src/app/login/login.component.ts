import { Component } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private auth: AuthService,
    private router: Router
  ) {
    this.form = this.fb.group({
      phone_number: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  submit() {
    if (this.form.invalid) {
      console.error("Form is invalid");
      return;
    }

    const credentials = {
      // Отправляем phone_number как username
      username: this.form.value.phone_number,
      password: this.form.value.password
    };

    this.auth.login(credentials).subscribe({
      next: (res) => {
        this.auth.saveToken(res.access);
        this.router.navigate(['/profile']);
      },
      error: (err) => {
        console.error('Login failed', err);
        alert('Login failed: ' + (err?.error?.message || 'An unknown error occurred'));
      }
    });
  }
}

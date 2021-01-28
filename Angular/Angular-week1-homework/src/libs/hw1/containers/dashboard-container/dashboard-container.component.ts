import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard-container',
  templateUrl: './dashboard-container.component.html',
  styleUrls: ['./dashboard-container.component.scss']
})
export class DashboardContainerComponent implements OnInit {
  cards: { name: string, body: string, email: string }[];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    //Loading posts from jsonplaceholder.typicode
    this.http.get("https://jsonplaceholder.typicode.com/comments").subscribe((comments: any) => {
      console.log(comments) // See incoming data in the browser console and remove this log
      // TODO: set cards array with valid objects
      this.cards = comments.map((element) => {
        return element;
      });
      // this.cards = comments. ... map? reduce? filter?
    })
  }

}

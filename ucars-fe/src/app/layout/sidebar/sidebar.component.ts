import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {

  menuItems: Array<any> = [];
  staticMenuItems: Array<any> = [];

  constructor() { }

  ngOnInit(): void {
    this.menuItems = [
      {
        name: 'Car Brand',
        route: '/car-brands',
        icon: '/assets/icons/clarity-car-line-icon.png',
        isActive: false,
        children: [],
      },
      {
        name: 'Folder',
        route: '/folder',
        icon: '/assets/icons/calendar-icon.png',
        isActive: false,
        isDivider: false,
        children: [
          {
            name: 'Item 1',
            route: '/item-1',
            icon: '/assets/icons/calendar-icon.png',
            isActive: false,
            isDivider: false,
            children: []
          },
          {
            name: 'Item 2',
            route: '/item-2',
            icon: '/assets/icons/calendar-icon.png',
            isActive: false,
            isDivider: false,
            children: []
          },
          {
            name: 'Item 3',
            route: '/item-3',
            icon: '/assets/icons/calendar-icon.png',
            isActive: false,
            isDivider: false,
            children: []
          },
          {
            name: 'Item 4',
            route: '/item-4',
            icon: '/assets/icons/calendar-icon.png',
            isActive: false,
            isDivider: false,
            children: []
          },
        ]
      },
      {
        name: 'Tasks',
        route: '/tasks',
        icon: '/assets/icons/calendar-icon.png',
        isActive: false,
        isDivider: false,
        children: []
      },
      {
        name: 'Modules',
        route: '/modules',
        icon: '/assets/icons/calendar-icon.png',
        isActive: false,
        isDivider: false,
        children: []
      },
      {
        name: 'Notifications',
        route: '/notifications',
        icon: '/assets/icons/calendar-icon.png',
        isActive: false,
        isDivider: false,
        children: []
      },
      {
        name: '',
        route: '',
        icon: '',
        isActive: false,
        isDivider: true,
        children: []
      },
      {
        name: 'Setting',
        route: '/setting',
        icon: '/assets/icons/setting-icon.png',
        isActive: false,
        isDivider: false,
        children: []
      },
    ];
  }

}

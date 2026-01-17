import React from 'react';
import { Bell, RefreshCw, Menu } from 'lucide-react';

const TopBar = ({ activeTab, fetchData, isLoading, setIsSidebarOpen }) => {
  return (
    <header className="navbar bg-base-100 shadow-sm px-4 md:px-8 z-10 border-b border-base-300 h-16 shrink-0">
      <div className="flex-none md:hidden mr-2">
        <button onClick={() => setIsSidebarOpen(true)} className="btn btn-square btn-ghost">
          <Menu className="h-6 w-6" />
        </button>
      </div>
      <div className="flex-1">
         <h2 className="text-xl font-bold capitalize opacity-80 tracking-wide">{activeTab.toLowerCase()}</h2>
      </div>
      
    </header>
  );
};

export default TopBar;